#!/usr/bin/env python3

import datetime
from typing import List

from xsdata.models.datatype import XmlDateTime

from nova import ErstellePreisAuskunftResponse, KlassenTypCode, PreisAuspraegung, \
    PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput
from ojp import OjpfareDelivery, FareResultStructure, FareProductStructure, TripFareResultStructure, \
    TypeOfFareClassEnumeration
from logger import log

def map_klasse_to_fareclass(klasse: KlassenTypCode) -> TypeOfFareClassEnumeration:
    if klasse == KlassenTypCode.KLASSE_1:
        return TypeOfFareClassEnumeration.FIRST
    elif klasse == KlassenTypCode.KLASSE_2:
        return TypeOfFareClassEnumeration.SECOND
    else:
        return None

def map_preis_auspraegung_to_trip_fare_result(preis_auspraegungen: List[PreisAuspraegung]) -> FareResultStructure:
    referenz = preis_auspraegungen[0].externe_verbindungs_referenz_id
    id, _, _ = referenz.split('_')

    tripfareresults = []
    for preis_auspraegung in preis_auspraegungen:
        _, from_leg_id, to_leg_id = preis_auspraegung.externe_verbindungs_referenz_id.split('_')
        tripfareresults.append(TripFareResultStructure(from_trip_leg_id_ref=from_leg_id, to_trip_leg_id_ref=to_leg_id,
                                fare_product=[FareProductStructure(fare_product_id=preis_auspraegung.produkt_nummer,
                                                                   fare_product_name=preis_auspraegung.produkt_nummer,
                                                                   fare_authority_ref='NOVA',
                                                                   fare_authority_text='NOVA',
                                                                   net_price=preis_auspraegung.preis.betrag,
                                                                   currency=preis_auspraegung.preis.waehrung,
                                                                   travel_class=map_klasse_to_fareclass(preis_auspraegung.produkt_einfluss_faktoren.klasse))]))

    return FareResultStructure(result_id=id, trip_fare_result=tripfareresults)


def map_nova_reply_to_ojp_fare_delivery(soap: PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput) -> OjpfareDelivery:
    if not soap.body.erstelle_preis_auskunft_response.preis_auskunft_response.preis_auspraegung:
        return False

    bonded_trips = {}
    for preis_auspraegung in soap.body.erstelle_preis_auskunft_response.preis_auskunft_response.preis_auspraegung:
        if preis_auspraegung.produkt_einfluss_faktoren.klasse == KlassenTypCode.KLASSENWECHSEL:
            continue

        referenz = preis_auspraegung.externe_verbindungs_referenz_id
        id, _, _ = referenz.split('_')
        bonded = bonded_trips.get(id, [])
        bonded.append(preis_auspraegung)
        bonded_trips[id] = bonded

    fareResults = [map_preis_auspraegung_to_trip_fare_result(x) for x in bonded_trips.values()]

    return OjpfareDelivery(response_timestamp=XmlDateTime.from_datetime(datetime.datetime.utcnow()), status=True, fare_result=fareResults)

def test_nova_to_ojp(soap: PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput) -> OjpfareDelivery:
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
    serializer = XmlSerializer(serializer_config)

    soap = parser.parse('nova_response.xml', PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput)
    if soap:
        ojp_fare_delivery = test_nova_to_ojp(soap)
        ojp_fare_delivery_xml = serializer.render(ojp_fare_delivery)
        log('generated/ojp_fare_reply.xml', ojp_fare_delivery_xml)
        print(ojp_fare_delivery_xml)