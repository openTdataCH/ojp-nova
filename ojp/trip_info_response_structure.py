from dataclasses import dataclass, field
from typing import List, Optional
from ojp.error_message_structure import ErrorMessageStructure
from ojp.trip_info_response_context_structure import TripInfoResponseContextStructure
from ojp.trip_info_result_structure import TripInfoResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripInfoResponseStructure:
    """
    :ivar error_message: Error messages related to the response as a
        whole.
    :ivar trip_info_response_context: Response context.
    :ivar trip_info_result: Result structure.
    """
    error_message: List[ErrorMessageStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_info_response_context: Optional[TripInfoResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "TripInfoResponseContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_info_result: Optional[TripInfoResultStructure] = field(
        default=None,
        metadata={
            "name": "TripInfoResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
