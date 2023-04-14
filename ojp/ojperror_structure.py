from dataclasses import dataclass, field
from typing import Optional
from ojp.availability_problem_type_enumeration import AvailabilityProblemTypeEnumeration
from ojp.exchange_points_problem_type_enumeration import ExchangePointsProblemTypeEnumeration
from ojp.fare_problem_type_enumeration import FareProblemTypeEnumeration
from ojp.international_text_structure import InternationalTextStructure
from ojp.line_information_problem_type_enumeration import LineInformationProblemTypeEnumeration
from ojp.location_problem_type_enumeration import LocationProblemTypeEnumeration
from ojp.ojpgeneric_problem_type_enumeration import OjpgenericProblemTypeEnumeration
from ojp.other_error_structure import OtherErrorStructure
from ojp.stop_event_problem_type_enumeration import StopEventProblemTypeEnumeration
from ojp.trip_info_problem_type_enumeration import TripInfoProblemTypeEnumeration
from ojp.trip_problem_type_enumeration import TripProblemTypeEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjperrorStructure(OtherErrorStructure):
    """
    Type for Error: OJP Error.

    :ivar trip_problem_type:
    :ivar trip_info_problem_type:
    :ivar stop_event_problem_type:
    :ivar ojpgeneric_problem_type:
    :ivar exchange_points_problem_type:
    :ivar location_problem_type:
    :ivar line_information_problem_type:
    :ivar fare_problem_type:
    :ivar availability_problem_type:
    :ivar error_type:
    :ivar details: Explanation of the problem.
    :ivar log_data: Additional log data.
    """
    class Meta:
        name = "OJPErrorStructure"

    trip_problem_type: Optional[TripProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TripProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_info_problem_type: Optional[TripInfoProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TripInfoProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    stop_event_problem_type: Optional[StopEventProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "StopEventProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    ojpgeneric_problem_type: Optional[OjpgenericProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "OJPGenericProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    exchange_points_problem_type: Optional[ExchangePointsProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ExchangePointsProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    location_problem_type: Optional[LocationProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LocationProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    line_information_problem_type: Optional[LineInformationProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LineInformationProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    fare_problem_type: Optional[FareProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FareProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    availability_problem_type: Optional[AvailabilityProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "AvailabilityProblemType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    error_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ErrorType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    details: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "Details",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    log_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "LogData",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
