from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from ojp.error_message_structure import ErrorMessageStructure
from ojp.trip_fare_result_structure import TripFareResultStructure
from ojp.trip_structure import TripStructure
from ojp.trip_summary_structure import TripSummaryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class MultiPointTripResultStructure:
    """
    Structure for a single trip result and its accompanying error messages.

    :ivar result_id: Id of this trip result for referencing purposes.
        Unique within multipoint-trip response.
    :ivar error_message: Error messages related to trip result.
    :ivar trip: Information on the trip.
    :ivar trip_summary:
    :ivar origin_wait_time: Additional wait time at origin of this trip.
    :ivar destination_wait_time: Additional wait time at destination of
        this trip.
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
    origin_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "OriginWaitTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    destination_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DestinationWaitTime",
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
