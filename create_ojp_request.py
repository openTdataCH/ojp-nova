#!/usr/bin/env python3

import datetime

from xsdata.models.datatype import XmlDateTime

from ojp import Ojp, Ojprequest, ServiceRequest, OjptripRequest, PlaceContextStructure, TripParamStructure, \
    PlaceRefStructure, InternationalTextStructure, NaturalLanguageStringStructure

def test_create_ojp_trip_request_simple_1() -> Ojp:
    origin='8507000'
    destination='8503000'
    starttime=datetime.datetime.utcnow()+ datetime.timedelta(days=10) #10 days in the future
    return test_create_ojp_trip_request_long(origin,destination,starttime)

def test_create_ojp_trip_request_simple_2() -> Ojp:
    origin='857868'
    destination='8574945'
    starttime=datetime.datetime.utcnow()+ datetime.timedelta(days=10) #10 days in the future
    return test_create_ojp_trip_request_long(origin,destination,starttime)


def test_create_ojp_trip_request_long(origin,destination,starttime) -> Ojp:
    starttime = starttime.isoformat() + "Z"
    starttime = XmlDateTime.from_string(starttime)

    return Ojp(ojprequest=
               Ojprequest(service_request=
                   ServiceRequest(requestor_ref="OJP2NOVA",
                                  request_timestamp=starttime,
                                  ojptrip_request=
                                  [OjptripRequest(
                                      request_timestamp=starttime,
                                      origin=[PlaceContextStructure(place_ref=
                                                                    PlaceRefStructure(stop_point_ref=str(origin),
                                                                                      location_name=InternationalTextStructure(text=NaturalLanguageStringStructure("origin"))),
                                                                    dep_arr_time=starttime)],
                                      destination=[PlaceContextStructure(place_ref=
                                                                         PlaceRefStructure(stop_point_ref=str(destination),
                                                                                           location_name=InternationalTextStructure(text=NaturalLanguageStringStructure("destination"))))
                                                                         ],
                                      params=TripParamStructure(number_of_results=5,
                                                                include_track_sections=False,
                                                                include_leg_projection=False,
                                                                include_turn_description=False,
                                                                include_intermediate_stops=True))])))
