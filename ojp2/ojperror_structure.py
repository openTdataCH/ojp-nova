from dataclasses import dataclass, field
from typing import Optional

from ojp2.availability_problem_type import AvailabilityProblemType
from ojp2.exchange_points_problem_type import ExchangePointsProblemType
from ojp2.fare_problem_type import FareProblemType
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.line_information_problem_type import LineInformationProblemType
from ojp2.location_problem_type import LocationProblemType
from ojp2.ojpgeneric_problem_type import OjpgenericProblemType
from ojp2.other_error_structure import OtherErrorStructure
from ojp2.status_problem_type import StatusProblemType
from ojp2.stop_event_problem_type import StopEventProblemType
from ojp2.trip_change_problem_type import TripChangeProblemType
from ojp2.trip_info_problem_type import TripInfoProblemType
from ojp2.trip_problem_type import TripProblemType

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjperrorStructure(OtherErrorStructure):
    """Type for Error: OJP Error.

    :ivar status_problem_type:
    :ivar trip_change_problem_type:
    :ivar trip_problem_type:
    :ivar trip_info_problem_type:
    :ivar stop_event_problem_type:
    :ivar ojpgeneric_problem_type:
    :ivar exchange_points_problem_type:
    :ivar location_problem_type:
    :ivar line_information_problem_type:
    :ivar fare_problem_type:
    :ivar availability_problem_type:
    :ivar details: Explanation of the problem.
    :ivar log_data: Additional log data.
    """

    class Meta:
        name = "OJPErrorStructure"

    status_problem_type: Optional[StatusProblemType] = field(
        default=None,
        metadata={
            "name": "StatusProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip_change_problem_type: Optional[TripChangeProblemType] = field(
        default=None,
        metadata={
            "name": "TripChangeProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip_problem_type: Optional[TripProblemType] = field(
        default=None,
        metadata={
            "name": "TripProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip_info_problem_type: Optional[TripInfoProblemType] = field(
        default=None,
        metadata={
            "name": "TripInfoProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    stop_event_problem_type: Optional[StopEventProblemType] = field(
        default=None,
        metadata={
            "name": "StopEventProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    ojpgeneric_problem_type: Optional[OjpgenericProblemType] = field(
        default=None,
        metadata={
            "name": "OJPGenericProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    exchange_points_problem_type: Optional[ExchangePointsProblemType] = field(
        default=None,
        metadata={
            "name": "ExchangePointsProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    location_problem_type: Optional[LocationProblemType] = field(
        default=None,
        metadata={
            "name": "LocationProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    line_information_problem_type: Optional[LineInformationProblemType] = (
        field(
            default=None,
            metadata={
                "name": "LineInformationProblemType",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            },
        )
    )
    fare_problem_type: Optional[FareProblemType] = field(
        default=None,
        metadata={
            "name": "FareProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    availability_problem_type: Optional[AvailabilityProblemType] = field(
        default=None,
        metadata={
            "name": "AvailabilityProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    details: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "Details",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    log_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogData",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
