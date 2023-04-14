from dataclasses import dataclass, field
from typing import List, Optional
from ojp.multi_trip_fare_result_structure import MultiTripFareResultStructure
from ojp.static_fare_result_structure import StaticFareResultStructure
from ojp.stop_fare_result_structure import StopFareResultStructure
from ojp.trip_fare_result_structure import TripFareResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FareResultStructure:
    """
    Wrapper element for Fare results.

    :ivar result_id: ID of this result.
    :ivar stop_fare_result: Stop-related Fare information.
    :ivar static_fare_result: Static Fare information.
    :ivar trip_fare_result: Fare and FareProducts for a given trip.
    :ivar multi_trip_fare_result: Fare and FareProducts for multiple
        trips.
    """
    result_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResultId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    stop_fare_result: Optional[StopFareResultStructure] = field(
        default=None,
        metadata={
            "name": "StopFareResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    static_fare_result: Optional[StaticFareResultStructure] = field(
        default=None,
        metadata={
            "name": "StaticFareResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_fare_result: List[TripFareResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "TripFareResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    multi_trip_fare_result: List[MultiTripFareResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "MultiTripFareResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
