from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_ojpservice_request_structure import (
    AbstractOjpserviceRequestStructure,
)
from ojp2.extensions_2 import Extensions2
from ojp2.fare_param_structure import FareParamStructure
from ojp2.multi_trip_fare_request_structure import (
    MultiTripFareRequestStructure,
)
from ojp2.place_fare_request_structure import PlaceFareRequestStructure
from ojp2.static_fare_request_structure import StaticFareRequestStructure
from ojp2.stop_fare_request_structure import StopFareRequestStructure
from ojp2.trip_fare_request_structure import TripFareRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpfareRequestStructure(AbstractOjpserviceRequestStructure):
    """
    :ivar stop_fare_request: A request for stop-related FARE
        information.
    :ivar place_fare_request: A request for place-related FARE
        information.
    :ivar static_fare_request: A request for general/static FARE
        information.
    :ivar trip_fare_request: A request to calculate the FARE information
        of a single trip.
    :ivar multi_trip_fare_request: A request to calculate aggregated
        FARE information of multiple single trips.
    :ivar params: Parameter to filter the response contents.
    :ivar extensions:
    """

    class Meta:
        name = "OJPFareRequestStructure"

    stop_fare_request: Optional[StopFareRequestStructure] = field(
        default=None,
        metadata={
            "name": "StopFareRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    place_fare_request: Optional[PlaceFareRequestStructure] = field(
        default=None,
        metadata={
            "name": "PlaceFareRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    static_fare_request: Optional[StaticFareRequestStructure] = field(
        default=None,
        metadata={
            "name": "StaticFareRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip_fare_request: Optional[TripFareRequestStructure] = field(
        default=None,
        metadata={
            "name": "TripFareRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    multi_trip_fare_request: Optional[MultiTripFareRequestStructure] = field(
        default=None,
        metadata={
            "name": "MultiTripFareRequest",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    params: Optional[FareParamStructure] = field(
        default=None,
        metadata={
            "name": "Params",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
