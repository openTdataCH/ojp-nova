from dataclasses import dataclass, field
from typing import List, Optional
from ojp.error_message_structure import ErrorMessageStructure
from ojp.trip_fare_result_structure import TripFareResultStructure
from ojp.trip_structure import TripStructure
from ojp.trip_summary_structure import TripSummaryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripResultStructure:
    """
    Structure for a single trip result and its accompanying error messages.

    :ivar result_id: Id of this trip result for referencing purposes.
        Unique within trip response.
    :ivar error_message: Error messages related to this trip result.
    :ivar trip: Detailed information on trip.
    :ivar trip_summary: Summary on trip. Only if requestor accepts
        deferrred delivery of trip details.
    :ivar trip_fare:
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
    error_message: List[ErrorMessageStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip: Optional[TripStructure] = field(
        default=None,
        metadata={
            "name": "Trip",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_summary: Optional[TripSummaryStructure] = field(
        default=None,
        metadata={
            "name": "TripSummary",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_fare: List[TripFareResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "TripFare",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
