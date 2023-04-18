#!/usr/bin/env python3

import datetime

from ojp import Ojp, Ojprequest, ServiceRequest, OjpfareRequest, FareParamStructure, PassengerCategoryEnumeration, \
    TypeOfFareClassEnumeration, FarePassengerStructure, TripFareRequestStructure, TripStructure

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.models.datatype import XmlDateTime

config = ParserConfig(
    base_url=None,
    process_xinclude=False,
    fail_on_unknown_properties=False,
    fail_on_unknown_attributes=False,
)

def parse_ojp(body: str) -> Ojp:
    parser = XmlParser(config)
    return parser.from_string(body, Ojp)

def map_to_individual_ojpfarerequest(trip: TripStructure, now: XmlDateTime) -> OjpfareRequest:
    return OjpfareRequest(
        request_timestamp=now,
        params=FareParamStructure(fare_authority_filter=["ch:1:NOVA"],
                                  passenger_category=[PassengerCategoryEnumeration.ADULT],
                                  travel_class=TypeOfFareClassEnumeration.SECOND,
                                  traveller=[
                                      FarePassengerStructure(passenger_category=PassengerCategoryEnumeration.ADULT,
                                                             age=25)]),
        trip_fare_request=TripFareRequestStructure(trip=trip)
    )

def map_ojp_trip_result_to_ojp_fare_request(ojp: Ojp) -> Ojp:
    if len(ojp.ojpresponse.service_delivery.ojptrip_delivery) != 1:
        return None

    now = datetime.datetime.utcnow()
    now = XmlDateTime.from_datetime(now)

    farerequest = []
    for ojptrip_delivery in ojp.ojpresponse.service_delivery.ojptrip_delivery:
        for trip_result in ojptrip_delivery.trip_result:
            farerequest += [map_to_inidividual_ojpfarerequest(trip_result.trip, now)]

    return Ojp(ojprequest=
               Ojprequest(service_request=
                   ServiceRequest(requestor_ref="OJP2NOVA",
                                  request_timestamp=now,
                                  ojpfare_request=farerequest)))
