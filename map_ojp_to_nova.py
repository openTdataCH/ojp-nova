#!/usr/bin/env python3
from nova import ErstellePreisAuskunft, VerbindungPreisAuskunftRequest, ClientIdentifier, CorrelationKontext, \
    TaxonomieFilter, TaxonomieKlassePfad, ReisendenInfoPreisAuskunft, ReisendenTypCode, VerbindungPreisAuskunft, \
    FahrplanVerbindungsSegment, VerkehrsMittelGattung, ZwischenHaltContextTripContext, \
    PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput
from logger import log
from ojp import Ojp, TimedLegStructure

def map_timed_leg_to_segment(timed_leg: TimedLegStructure) -> FahrplanVerbindungsSegment:
    einstieg = timed_leg.leg_board.stop_point_ref
    ausstieg = timed_leg.leg_alight.stop_point_ref
    abfahrts_zeit = timed_leg.leg_board.service_departure.timetabled_time
    ankunfts_zeit = timed_leg.leg_alight.service_arrival.timetabled_time
    line_ref = timed_leg.service.line_ref
    operator_ref = timed_leg.service.operator_ref  # needs to be processed afterwards to get the verwaltungs_code
    gattungs_code = timed_leg.service.mode.short_name.text.value  # is correct, but a bit of a hack

    # unfortunately it is not in line_ref, but in Extension/ojp:PublishedJourneyNumber
    _, verkehrs_mittel_nummer, _ = line_ref.split(':')
    # This is an other hack.
    verkehrs_mittel_nummer = ''.join(filter(lambda x: x.isdigit(), verkehrs_mittel_nummer))

    try:
        # Set verkehrs_mittel_nummer to timed_leg.extension.publishedjourneynumber?
        verkehrs_mittel_nummer = [x.children[0].text for x in timed_leg.extension.children if x.qname == '{http://www.vdv.de/ojp}PublishedJourneyNumber'][0]
    except:
        pass

    # Uses ojp:OperatorRef in service
    verwaltungs_code = "{:06}".format(int(operator_ref.split(':')[1])) # takes e.g. ojp:11 and makes 000011 out of it

    leg_intermediates = timed_leg.leg_intermediates
    zwischenhalten = [timed_leg.leg_board.stop_point_ref] + [leg_intermediate.stop_point_ref
                      for leg_intermediate in leg_intermediates] + [timed_leg.leg_alight.stop_point_ref]

    return FahrplanVerbindungsSegment(einstieg=int(einstieg), ausstieg=int(ausstieg),
                               verwaltungs_code=verwaltungs_code,
                               abfahrts_zeit=abfahrts_zeit,
                               ankunfts_zeit=ankunfts_zeit,
                               verkehrs_mittel=VerkehrsMittelGattung(
                                   gattungs_code=gattungs_code,
                                   verkehrs_mittel_nummer=int(verkehrs_mittel_nummer)),
                               zwischen_halt_context=[FahrplanVerbindungsSegment.ZwischenHaltContext(
                                       uic_code=int(zwischenhalt),
                                       trip_context=ZwischenHaltContextTripContext.PLANNED) for zwischenhalt in zwischenhalten]
                               )

def map_fare_request_to_nova_request(ojp: Ojp, age: int=30) -> PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput:
    if not (ojp.ojprequest and ojp.ojprequest.service_request and ojp.ojprequest.service_request.ojpfare_request
            and len(ojp.ojprequest.service_request.ojpfare_request) > 0 and ojp.ojprequest.service_request.ojpfare_request[0].trip_fare_request
            and ojp.ojprequest.service_request.ojpfare_request[0].trip_fare_request.trip
            and len(ojp.ojprequest.service_request.ojpfare_request[0].trip_fare_request.trip.trip_leg) > 0):
        return False

    try:
        age = ojp.ojprequest.service_request.ojpfare_request[0].params.traveller[0].age
    except:
        pass

    verbindungen = []
    for fare_request in ojp.ojprequest.service_request.ojpfare_request:
        legs = fare_request.trip_fare_request.trip.trip_leg
        externeVerbindungsReferenzId = fare_request.trip_fare_request.trip.trip_id
        segments = []
        leg_start = None
        leg_end = None
        for leg in legs:

            # Only handled TimedLegs, everything else we should ignore (for now)
            if leg.timed_leg is None:
                continue

            # To get the first TimedLeg and last TimedLeg to reply with the leg range in the FareResult
            leg_id = leg.leg_id
            if not leg_start:
                leg_start = leg_id
            leg_end = leg_id

            segments += [map_timed_leg_to_segment(leg.timed_leg)]

        verbindungen += [VerbindungPreisAuskunft(externe_verbindungs_referenz_id=externeVerbindungsReferenzId + "_" + leg_start + "_" + leg_end, segment_hin_fahrt=segments)]

    return PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput(body=PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput.Body(erstelle_preis_auskunft=ErstellePreisAuskunft(
        preis_auskunft_request=VerbindungPreisAuskunftRequest(kunden_segmente_gruppieren=False,
                                                              client_identifier=ClientIdentifier(
                                                                  leistungs_vermittler=11, kanal_code=41,
                                                                  verkaufs_stelle=16437, vertriebs_punkt=16437,
                                                                  verkaufs_geraete_id="236"),
                                                              correlation_kontext=CorrelationKontext(
                                                                  correlation_id="87482634-560b-4da3-b6a1-155c37490fed",
                                                                  geschaefts_prozess_id="1781786f-57ba-4e9a-bc29-287e2aa97f9a"),
                                                              angebots_filter=[TaxonomieFilter(
                                                                  produkt_taxonomie="Basistaxonomie",
                                                                  taxonomie_klasse_pfad=[TaxonomieKlassePfad(
                                                                      klassen_name="Einzelbillette")])],
                                                              reisender=[ReisendenInfoPreisAuskunft(alter=age,
                                                                                                    externe_reisenden_referenz_id="1234",
                                                                                                    reisenden_typ=ReisendenTypCode.PERSON)],
                                                              verbindung=verbindungen
                                                              ))))

def test_ojp_fare_request_to_nova_request(ojp: Ojp) -> PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput:
    from xsdata.formats.dataclass.serializers import XmlSerializer
    from xsdata.formats.dataclass.serializers.config import SerializerConfig

    serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
    serializer = XmlSerializer(serializer_config)

    nova_request = map_fare_request_to_nova_request(ojp)
    nova_request_xml = serializer.render(nova_request)
    log('generated/nova_request.xml',nova_request_xml)
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
    ojp = parser.parse('generated/ojp_fare_request.xml', Ojp)

    if ojp:
        print(test_ojp_fare_request_to_nova_request(ojp))
