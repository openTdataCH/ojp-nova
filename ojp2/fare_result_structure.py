from dataclasses import dataclass, field
from typing import Optional

from ojp2.multi_trip_fare_result_structure import MultiTripFareResultStructure
from ojp2.ojperror_structure import OjperrorStructure
from ojp2.place_fare_result_structure import PlaceFareResultStructure
from ojp2.static_fare_result_structure import StaticFareResultStructure
from ojp2.stop_fare_result_structure import StopFareResultStructure
from ojp2.trip_fare_result_structure import TripFareResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FareResultStructure:
    """
    Wrapper element for Fare results.

    :ivar id: ID of this result.
    :ivar error_condition: Problems related to this FARE result.
    :ivar fare_estimated: Whether the fare is only estimated by the
        service. Estimated can mean different things: For example, the
        fare may vary depending on age, PassengerCategory, FareClass,
        EntitlementProducts. It can also mean that the fare structure
        used by the service is not entirely accurate or that other
        factors, such as the time a shared vehicle is used, need to be
        factored into the price. As a rule, the price should then be
        given as an approximate and probably lower limit of the actual
        price. Default is TRUE.
    :ivar stop_fare_result: Stop-related Fare information.
    :ivar place_fare_result: Place-related Fare information.
    :ivar static_fare_result: Static Fare information.
    :ivar trip_fare_result: Fare and FareProducts for a given trip.
    :ivar multi_trip_fare_result: Fare and FareProducts for multiple
        trips.
    """

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    error_condition: list[OjperrorStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    fare_estimated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FareEstimated",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    stop_fare_result: Optional[StopFareResultStructure] = field(
        default=None,
        metadata={
            "name": "StopFareResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    place_fare_result: Optional[PlaceFareResultStructure] = field(
        default=None,
        metadata={
            "name": "PlaceFareResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    static_fare_result: Optional[StaticFareResultStructure] = field(
        default=None,
        metadata={
            "name": "StaticFareResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip_fare_result: list[TripFareResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "TripFareResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    multi_trip_fare_result: list[MultiTripFareResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "MultiTripFareResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
