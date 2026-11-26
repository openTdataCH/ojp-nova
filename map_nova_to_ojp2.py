#!/usr/bin/env python3

from datetime import UTC, datetime
from decimal import Decimal

from xsdata.models.datatype import XmlDateTime

import xml_logger
from api.errors import InvalidNovaResponseError
from configuration import VATRATE
from fare_products import products
from nova import (
    KlassenTypCode,
    PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput,
    PreisAuspraegung,
)
from ojp2 import (
    FareClassEnumeration,
    FareProductStructure,
    FareResultStructure,
    OjpfareDelivery,
    TripFareResultStructure,
)


def map_klasse_to_fareclass(klasse: KlassenTypCode) -> FareClassEnumeration | None:
    if klasse == KlassenTypCode.KLASSE_1:
        return FareClassEnumeration.FIRST_CLASS
    elif klasse == KlassenTypCode.KLASSE_2:
        return FareClassEnumeration.SECOND_CLASS
    else:
        return None


def map_preis_auspraegung_to_trip_fare_result(preis_auspraegungen: list[PreisAuspraegung]) -> FareResultStructure:
    referenz = preis_auspraegungen[0].externe_verbindungs_referenz_id
    id, _, _ = referenz.split('_')

    tripfareresults = []
    for preis_auspraegung in preis_auspraegungen:
        _, from_leg_id, to_leg_id = preis_auspraegung.externe_verbindungs_referenz_id.split('_')
        required_card = []
        if preis_auspraegung.produkt_einfluss_faktoren.kunden_segment.kunden_segment_code == "HALBTAX":
            required_card = ["HTA"]
        fare_product_name = products.get(str(preis_auspraegung.produkt_nummer), str(preis_auspraegung.produkt_nummer))  # name or number if none
        tripfareresults.append(
            TripFareResultStructure(
                from_leg_id_ref=from_leg_id,
                to_leg_id_ref=to_leg_id,
                fare_product=[
                    FareProductStructure(
                        fare_product_id=preis_auspraegung.produkt_nummer,
                        fare_product_name=fare_product_name,
                        fare_authority_ref='ch:1:sboid:101704',
                        fare_authority_text='Alliance SwissPass',
                        price=preis_auspraegung.preis.betrag,
                        net_price=round(float(preis_auspraegung.preis.betrag) * (1.0 - VATRATE / 100), 2),
                        currency=preis_auspraegung.preis.waehrung,
                        required_card=required_card,
                        vat_rate=Decimal(VATRATE).quantize(Decimal("0.1")),
                        fare_class=map_klasse_to_fareclass(preis_auspraegung.produkt_einfluss_faktoren.klasse),
                    )
                ],
            )
        )

    return FareResultStructure(id=id, trip_fare_result=tripfareresults)


def map_nova_reply_to_ojp_fare_delivery(soap: PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput) -> OjpfareDelivery | None:
    if not soap.body.erstelle_preis_auskunft_response.preis_auskunft_response.preis_auspraegung:
        raise InvalidNovaResponseError()

    bonded_trips: dict[str, PreisAuspraegung] = {}
    for preis_auspraegung in soap.body.erstelle_preis_auskunft_response.preis_auskunft_response.preis_auspraegung:
        if preis_auspraegung.produkt_einfluss_faktoren.klasse == KlassenTypCode.KLASSENWECHSEL:
            continue

        referenz = preis_auspraegung.externe_verbindungs_referenz_id
        id, _, _ = referenz.split('_')
        bonded = bonded_trips.get(id, [])
        bonded.append(preis_auspraegung)
        bonded_trips[id] = bonded

    fareResults = [map_preis_auspraegung_to_trip_fare_result(x) for x in bonded_trips.values()]

    return OjpfareDelivery(response_timestamp=XmlDateTime.from_datetime(datetime.now(UTC)), status=True, fare_result=fareResults)


def test_nova_to_ojp2(soap: PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput) -> OjpfareDelivery | None:
    ojp_fare_delivery = map_nova_reply_to_ojp_fare_delivery(soap)
    return ojp_fare_delivery


if __name__ == '__main__':
    from xsdata.formats.dataclass.parsers import XmlParser
    from xsdata.formats.dataclass.parsers.config import ParserConfig
    from xsdata.formats.dataclass.serializers import XmlSerializer
    from xsdata.formats.dataclass.serializers.config import SerializerConfig

    parser_config = ParserConfig(
        base_url=None,
        process_xinclude=False,
        fail_on_unknown_properties=False,
        fail_on_unknown_attributes=False,
    )
    parser = XmlParser(parser_config)

    serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
    serializer = XmlSerializer(config=serializer_config)

    soap = parser.parse(xml_logger.path('nova_response.xml'), PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput)
    if soap:
        ojp_fare_delivery = test_nova_to_ojp2(soap)
        ojp_fare_delivery_xml = serializer.render(ojp_fare_delivery)
        xml_logger.log_serialized('ojp_fare_reply.xml', ojp_fare_delivery_xml)
        print(ojp_fare_delivery_xml)
