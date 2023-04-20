#!/usr/bin/env python3

import datetime

from xsdata.models.datatype import XmlDateTime

from ojp import Ojp, Ojprequest, ServiceRequest, OjptripRequest, PlaceContextStructure, TripParamStructure, \
    PlaceRefStructure, InternationalTextStructure, NaturalLanguageStringStructure

def test_create_ojp_trip_request() -> Ojp:
    now = datetime.datetime.utcnow().isoformat() + "Z"
    now = XmlDateTime.from_string(now)

    return Ojp(ojprequest=
               Ojprequest(service_request=
                   ServiceRequest(requestor_ref="OJP2NOVA",
                                  request_timestamp=now,
                                  ojptrip_request=
                                  [OjptripRequest(
                                      request_timestamp=now,
                                      origin=[PlaceContextStructure(place_ref=
                                                                    PlaceRefStructure(stop_point_ref=str(8507000),
                                                                                      location_name=InternationalTextStructure(text=NaturalLanguageStringStructure("Bern"))),
                                                                    dep_arr_time=now)],
                                      destination=[PlaceContextStructure(place_ref=
                                                                         PlaceRefStructure(stop_point_ref=str(8503000),
                                                                                           location_name=InternationalTextStructure(text=NaturalLanguageStringStructure("Zurich"))))
                                                                         ],
                                      params=TripParamStructure(number_of_results=5,
                                                                include_track_sections=False,
                                                                include_leg_projection=False,
                                                                include_turn_description=False,
                                                                include_intermediate_stops=True))])))
