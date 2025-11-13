#!/usr/bin/env python3

import datetime
from typing import Optional

from configuration import USE_HTA
from ojp import Ojp, Ojprequest, ServiceRequest, OjpfareRequest, FareParamStructure, PassengerCategoryEnumeration, \
    TypeOfFareClassEnumeration, FarePassengerStructure, TripFareRequestStructure, TripStructure, \
    OjptripDeliveryStructure

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.models.datatype import XmlDateTime

from support import OJPError

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
    travellers=[]
    if USE_HTA:
        travellers.append(FarePassengerStructure(age=25,entitlement_product = ["HTA"]))
    else:
        travellers.append(FarePassengerStructure(passenger_category=PassengerCategoryEnumeration.ADULT,entitlement_product = []))

    return OjpfareRequest(
        request_timestamp=now,
        params=FareParamStructure(fare_authority_filter=["ch:1:NOVA"],
                                  passenger_category=[PassengerCategoryEnumeration.ADULT],
                                  travel_class=TypeOfFareClassEnumeration.SECOND,
                                  traveller=travellers),
        trip_fare_request=TripFareRequestStructure(trip=trip))

# def map_to_individual_ojptriprefinerequest(trip_result: TripResultStructure, now: XmlDateTime) -> OjptripRefineRequest:
#     return OjptripRefineRequest(
#         request_timestamp=now,
#         refine_params=TripRefineParamStructure(include_intermediate_stops=True),
#         trip_result=trip_result
#     )

# TODO: This will not work until v1.1
# def map_ojp_trip_result_to_ojp_refine_request(ojp: Ojp) -> Ojp:
#     if len(ojp.ojpresponse.service_delivery.ojptrip_delivery) != 1:
#         return None
#
#    now = datetime.datetime.utcnow()
#    now = XmlDateTime.from_datetime(now)
#
#    refinerequest = []
#    for ojptrip_delivery in ojp.ojpresponse.service_delivery.ojptrip_delivery:
#        for trip_result in ojptrip_delivery.trip_result:
#            refinerequest += [map_to_individual_ojptriprefinerequest(trip_result, now)]
#
#    return Ojp(ojprequest=
#               Ojprequest(service_request=
#                   ServiceRequest(requestor_ref="OJP2NOVA",
#                                  request_timestamp=now,
#                                  ojprefinement_request=refinerequest)))

def preprocess_stops_to_commercial_stops(delivery: OjptripDeliveryStructure) -> OjptripDeliveryStructure:
    #prepocessing every StopPointRef is replaced with the highest level of parent for the processing in fares
    #parse context and create a dictionary of the highest parent
    parent = {}
    #TODO we do it once only, but in future we might to change it
    if not delivery.trip_response_context:
        return delivery
    if delivery.trip_response_context.places:
        for place in delivery.trip_response_context.places.location:
            if place.stop_point is not None:
                if place.stop_point.parent_ref is not None:
                    parent[place.stop_point.stop_point_ref]=place.stop_point.parent_ref
    #foreach trip
        for trip_result in delivery.trip_result:
            if trip_result.trip.trip_leg is None:
                raise OJPError("ERR104: No legs in Trip.")
            for leg in trip_result.trip.trip_leg:
                if leg.timed_leg is None:
                    continue
                # if the timed leg is an on demand bus -> also ignore
                if leg.timed_leg.service.mode is None:
                    continue
                if leg.timed_leg.service.mode.bus_submode == "demandResponsive":
                    # we can't deal with demandResponsive in NOVA currently.
                    continue
                ## only timed. we now replace the stop_point_ref with the parent
                leg.timed_leg.leg_board.stop_point_ref = parent.get(leg.timed_leg.leg_board.stop_point_ref,leg.timed_leg.leg_board.stop_point_ref)
                leg.timed_leg.leg_alight.stop_point_ref = parent.get(leg.timed_leg.leg_alight.stop_point_ref,leg.timed_leg.leg_alight.stop_point_ref)
                leg_intermediates = leg.timed_leg.leg_intermediates
                for leg_intermediate in leg_intermediates:
                    leg_intermediate.stop_point_ref = parent.get(leg_intermediate.stop_point_ref,leg_intermediate.stop_point_ref)
    return delivery

def map_ojp_trip_result_to_ojp_fare_request(ojp: Ojp) -> Optional[Ojp]:
    if ojp.ojpresponse is None or ojp.ojpresponse.service_delivery is None or ojp.ojpresponse.service_delivery.ojptrip_delivery is None or len(ojp.ojpresponse.service_delivery.ojptrip_delivery) != 1:
        return None

    now1 = datetime.datetime.utcnow()
    now = XmlDateTime.from_datetime(now1)


    farerequest = []
    if ojp.ojpresponse.service_delivery is None or ojp.ojpresponse.service_delivery.ojptrip_delivery is None :
        OJPError("ERR106: No service delivery could be genrated")
    for ojptrip_delivery in ojp.ojpresponse.service_delivery.ojptrip_delivery:
        # preprocess trip result to translate the quays to the commercial stop
        ojptrip_delivery=preprocess_stops_to_commercial_stops(ojptrip_delivery)
        for trip_result in ojptrip_delivery.trip_result:
            if trip_result.trip:
                farerequest += [map_to_individual_ojpfarerequest(trip_result.trip, now)]

    return Ojp(ojprequest=
               Ojprequest(service_request=
                   ServiceRequest(requestor_ref="OJP2NOVA",
                                  request_timestamp=now,
                                  ojpfare_request=farerequest)))
