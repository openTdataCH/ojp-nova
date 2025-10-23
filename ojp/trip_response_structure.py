from dataclasses import dataclass, field
from typing import List, Optional
from ojp.error_message_structure import ErrorMessageStructure
from ojp.trip_response_context_structure import TripResponseContextStructure
from ojp.trip_result_structure import TripResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripResponseStructure:
    """
    :ivar error_message: Error messages related to the trip request as a
        whole.
    :ivar trip_response_context: Context to hold trip response objects
        that occur frequently.
    :ivar trip_result: The trip results found by the server.
    """
    error_message: List[ErrorMessageStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_response_context: Optional[TripResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "TripResponseContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    trip_result: List[TripResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "TripResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
