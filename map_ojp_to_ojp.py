#!/usr/bin/env python3

import datetime

from ojp import Ojp, Ojprequest, ServiceRequest, OjpfareRequest, FareParamStructure, PassengerCategoryEnumeration, \
    TypeOfFareClassEnumeration, FarePassengerStructure, TripFareRequestStructure, TripStructure, OjptripRequest, \
    TripResultStructure

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.models.datatype import XmlDateTime

from ojp.ojptrip_refine_request import OjptripRefineRequest
from ojp.trip_refine_param_structure import TripRefineParamStructure

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

def map_to_individual_ojptriprefinerequest(trip_result: TripResultStructure, now: XmlDateTime) -> OjptripRefineRequest:
    return OjptripRefineRequest(
        request_timestamp=now,
        refine_params=TripRefineParamStructure(include_intermediate_stops=True),
        trip_result=trip_result
    )

# TODO: This will not work until v1.1
def map_ojp_trip_result_to_ojp_refine_request(ojp: Ojp) -> Ojp:
    if len(ojp.ojpresponse.service_delivery.ojptrip_delivery) != 1:
        return None

    now = datetime.datetime.utcnow()
    now = XmlDateTime.from_datetime(now)

    refinerequest = []
    for ojptrip_delivery in ojp.ojpresponse.service_delivery.ojptrip_delivery:
        for trip_result in ojptrip_delivery.trip_result:
            refinerequest += [map_to_individual_ojptriprefinerequest(trip_result, now)]

    return Ojp(ojprequest=
               Ojprequest(service_request=
                   ServiceRequest(requestor_ref="OJP2NOVA",
                                  request_timestamp=now,
                                  ojprefinement_request=refinerequest)))

def map_ojp_trip_result_to_ojp_fare_request(ojp: Ojp) -> Ojp:
    if len(ojp.ojpresponse.service_delivery.ojptrip_delivery) != 1:
        return None

    now = datetime.datetime.utcnow()
    now = XmlDateTime.from_datetime(now)

    farerequest = []
    for ojptrip_delivery in ojp.ojpresponse.service_delivery.ojptrip_delivery:
        for trip_result in ojptrip_delivery.trip_result:
            farerequest += [map_to_individual_ojpfarerequest(trip_result.trip, now)]

    return Ojp(ojprequest=
               Ojprequest(service_request=
                   ServiceRequest(requestor_ref="OJP2NOVA",
                                  request_timestamp=now,
                                  ojpfare_request=farerequest)))
