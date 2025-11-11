#!/usr/bin/env python3
from typing import List, Optional
from nova import ErstellePreisAuskunft, VerbindungPreisAuskunftRequest, ClientIdentifier, CorrelationKontext, \
    TaxonomieFilter, TaxonomieKlassePfad, ReisendenInfoPreisAuskunft, ReisendenTypCode, VerbindungPreisAuskunft, \
    FahrplanVerbindungsSegment, VerkehrsMittelGattung, ZwischenHaltContextTripContext, \
    PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput, EmptyType
from ojp2 import Ojp, TimedLegStructure, FarePassengerStructure, PassengerCategoryEnumeration, \
    EntitlementProductStructure
from support import OJPError, process_operating_ref_ojp2,sloid2didok
import logging
import xml_logger
import random

logger = logging.getLogger(__name__)

def map_timed_leg_to_segment(timed_leg: TimedLegStructure) -> FahrplanVerbindungsSegment:
    einstieg = sloid2didok(timed_leg.leg_board.stop_point_ref)
    ausstieg = sloid2didok(timed_leg.leg_alight.stop_point_ref)
    abfahrts_zeit = timed_leg.leg_board.service_departure.timetabled_time
    ankunfts_zeit = timed_leg.leg_alight.service_arrival.timetabled_time
    line_ref = timed_leg.service.line_ref.value
    operator_ref = timed_leg.service.operator_ref  # needs to be processed afterwards to get the verwaltungs_code
    gattungs_code = timed_leg.service.mode.short_name.text[0].value  # is correct, but a bit of a hack

    # unfortunately it is not in line_ref, but in Extension/ojp:PublishedJourneyNumber
    _, verkehrs_mittel_nummer, _ = line_ref.split(':')
    # This is an other hack.
    verkehrs_mittel_nummer = ''.join(filter(lambda x: x.isdigit(), verkehrs_mittel_nummer))
    try:
        # Set verkehrs_mittel_nummer to timed_leg.extension.publishedjourneynumber?
        verkehrs_mittel_nummer = [x.children[0].text for x in timed_leg.extension.childen if x.qname == '{http://www.vdv.de/ojp}PublishedJourneyNumber'][0]
    except:
        pass

    verwaltungs_code= process_operating_ref_ojp2(operator_ref)

    leg_intermediates = timed_leg.leg_intermediate
    zwischenhalten = [sloid2didok(timed_leg.leg_board.stop_point_ref)] + [sloid2didok(leg_intermediate.stop_point_ref)
                      for leg_intermediate in leg_intermediates] + [sloid2didok(timed_leg.leg_alight.stop_point_ref)]

    #handling of Tariff code TC
    attr2=timed_leg.service.attribute
    tariff_code=""
    for attr in attr2:
        attr_text= attr.user_text.text
        if attr_text[0].value.startswith("TC-"):
            #tariff code found in OJP data
            tariff_code=attr_text[0].value[3:]
    if tariff_code=="":
        return FahrplanVerbindungsSegment(einstieg=int(einstieg), ausstieg=int(ausstieg),
                                          verwaltungs_code=verwaltungs_code,
                                          abfahrts_zeit=abfahrts_zeit,
                                          ankunfts_zeit=ankunfts_zeit,
                                          verkehrs_mittel=VerkehrsMittelGattung(
                                              gattungs_code=gattungs_code,
                                              verkehrs_mittel_nummer=int(verkehrs_mittel_nummer)),
                                          zwischen_halt_context=[FahrplanVerbindungsSegment.ZwischenHaltContext(
                                              uic_code=int(zwischenhalt),
                                              trip_context=ZwischenHaltContextTripContext.PLANNED) for zwischenhalt in
                                              zwischenhalten]
                                          )

    return FahrplanVerbindungsSegment(einstieg=int(einstieg), ausstieg=int(ausstieg),
                               verwaltungs_code=verwaltungs_code,
                               info_plus_tarif_code =tariff_code,
                               abfahrts_zeit=abfahrts_zeit,
                               ankunfts_zeit=ankunfts_zeit,
                               verkehrs_mittel=VerkehrsMittelGattung(
                                   gattungs_code=gattungs_code,
                                   verkehrs_mittel_nummer=int(verkehrs_mittel_nummer)),
                               zwischen_halt_context=[FahrplanVerbindungsSegment.ZwischenHaltContext(
                                       uic_code=int(zwischenhalt),
                                       trip_context=ZwischenHaltContextTripContext.PLANNED) for zwischenhalt in zwischenhalten]
                               )

def map_fare_request_to_nova_request(ojp: Ojp, age: int=30) -> Optional[PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput]:
    if not (ojp.ojprequest and ojp.ojprequest.service_request and ojp.ojprequest.service_request.ojpfare_request
            and len(ojp.ojprequest.service_request.ojpfare_request) > 0 and ojp.ojprequest.service_request.ojpfare_request[0].trip_fare_request
            and ojp.ojprequest.service_request.ojpfare_request[0].trip_fare_request.trip
            and len(ojp.ojprequest.service_request.ojpfare_request[0].trip_fare_request.trip.leg) > 0):
        return None

    try:
        if ojp.ojprequest.service_request.ojpfare_request[0].params.traveller is None:
            travellers = []
            travellers.append(FarePassengerStructure(age=25, entitlement_products=[EntitlementProductStructure(entitlement_product_ref="HTA",entitlement_product_name="HTA",fare_authority_ref="NOVA")]))
        else:
            age = ojp.ojprequest.service_request.ojpfare_request[0].params.traveller[0].age
            travellers = ojp.ojprequest.service_request.ojpfare_request[0].params.traveller
    except Exception:
        pass

    verbindungen = []
    for fare_request in ojp.ojprequest.service_request.ojpfare_request:
        legs = fare_request.trip_fare_request.trip.leg
        externeVerbindungsReferenzId = fare_request.trip_fare_request.trip.id
        segments = []
        reisende:List[ReisendenInfoPreisAuskunft] = []
        leg_start = None
        leg_end = None
        leg_nr=0
        for leg in legs:
            leg_nr = leg_nr + 1
            # Only handled TimedLegs, everything else we should ignore (for now)
            if leg.continuous_leg is not None:
                # We can't price continuous legs. This in many cases may be correct, but not for sharing.
                continue
            if leg.timed_leg is None:
                continue
            # if the timed leg is an on demand bus -> also ignore
            if leg.timed_leg.service.mode is None:
                continue
            if leg.timed_leg.service.mode.bus_submode and leg.timed_leg.service.mode.bus_submode.value == "demandAndResponseBus":
                #we can't deal with demandResponsive in NOVA currently.
                continue
            # To get the first TimedLeg and last TimedLeg to reply with the leg range in the FareResult
            leg_id = leg.id
            if not leg_start:
                leg_start = leg_id
            leg_end = leg_id
            segments += [map_timed_leg_to_segment(leg.timed_leg)]
        if leg_start is None:
            #no pricable legs found.
            raise OJPError("no pricable legs found.")

        verbindungen += [VerbindungPreisAuskunft(externe_verbindungs_referenz_id=externeVerbindungsReferenzId + "_" + leg_start + "_" + leg_end, segment_hin_fahrt=segments)]
        reisende =[]
        for traveler in travellers:
            # we only do one for the time being TODO
            r_alter=25
            if traveler.age is None:
                r_alter=25
            else:
                r_alter=traveler.age
            r_typ = ReisendenTypCode.PERSON
            if traveler.passenger_category is None:
                r_typ =ReisendenTypCode.PERSON
            elif traveler.passenger_category == PassengerCategoryEnumeration.DOG:
                r_typ = ReisendenTypCode.HUND
            elif traveler.passenger_category == PassengerCategoryEnumeration.BICYCLE:
                r_typ = ReisendenTypCode.VELO
            else:
                r_typ = ReisendenTypCode.PERSON
            digits = "0123456789"
            r_referenz= ''.join(random.choice(digits) for _ in range(6))
            # we only process HTA for the time being!
            reisender = ReisendenInfoPreisAuskunft(alter=r_alter,
                                                   externe_reisenden_referenz_id=r_referenz,
                                                   reisenden_typ=r_typ,
                                                   ermaessigungs_karte_code=[])

            for entitlement_product in traveler.entitlement_products.entitlement_product:
                if entitlement_product.entitlement_product_ref=="HTA":
                    reisender = ReisendenInfoPreisAuskunft(alter=r_alter,
                                                           externe_reisenden_referenz_id=r_referenz,
                                                           reisenden_typ=r_typ,
                                                           ermaessigungs_karte_code=["HTA"])
            reisende.append(reisender)
    return PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput(
        body=PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput.Body(
            erstelle_preis_auskunft=ErstellePreisAuskunft(
                preis_auskunft_request=VerbindungPreisAuskunftRequest(kunden_segmente_gruppieren=False,
                                                                      client_identifier=ClientIdentifier(
                                                                          leistungs_vermittler=11, kanal_code=41,
                                                                          verkaufs_stelle=16437, vertriebs_punkt=16437,
                                                                          verkaufs_geraete_id="236"),
                                                                      correlation_kontext=CorrelationKontext(
                                                                          correlation_id="87482634-560b-4da3-b6a1-155c37490fed",
                                                                          geschaefts_prozess_id="1781786f-57ba-4e9a-bc29-287e2aa97f9a"),
                                                                      angebots_filter=[TaxonomieFilter(
                                                                          produkt_taxonomie="SBB Preisauskunft",
                                                                          taxonomie_klasse_pfad=[TaxonomieKlassePfad(EmptyType())])],
                                                                      reisender=reisende,
                                                                      verbindung=verbindungen
                                                                      ))))

def test_ojp2_fare_request_to_nova_request(ojp: Ojp) -> PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput:
    from xsdata.formats.dataclass.serializers import XmlSerializer
    from xsdata.formats.dataclass.serializers.config import SerializerConfig

    serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
    serializer = XmlSerializer(config=serializer_config)

    nova_request = map_fare_request_to_nova_request(ojp)
    if nova_request is None or not nova_request:
        logger.error("Was not able to generate NOVA request from OJPFare Request")
        raise OJPError("Was not able to generate NOVA request from OJPFare Request:\n")
    xml_logger.log_object_as_xml('nova_request_2.0.xml',nova_request)
    return nova_request

if __name__ == '__main__':
    from xsdata.formats.dataclass.parsers import XmlParser
    from xsdata.formats.dataclass.parsers.config import ParserConfig

    parser_config = ParserConfig(
        base_url=None,
        process_xinclude=False,
        fail_on_unknown_properties=False,
        fail_on_unknown_attributes=False,
    )
    parser = XmlParser(parser_config)
    ojp = parser.parse(xml_logger.path('ojp_fare_request_2.0.xml'), Ojp)

    if ojp:
        print(test_ojp2_fare_request_to_nova_request(ojp))
