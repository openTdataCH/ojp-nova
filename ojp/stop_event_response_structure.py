from dataclasses import dataclass, field
from typing import List, Optional
from ojp.error_message_structure import ErrorMessageStructure
from ojp.stop_event_response_context_structure import StopEventResponseContextStructure
from ojp.stop_event_result_structure import StopEventResultStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopEventResponseStructure:
    """
    :ivar error_message: Error messages that refer to the stop event
        response as a whole.
    :ivar stop_event_response_context: Container for data that is
        referenced multiple times.
    :ivar stop_event_result: Enclosing element for stop event data.
    """
    error_message: List[ErrorMessageStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorMessage",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    stop_event_response_context: Optional[StopEventResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "StopEventResponseContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    stop_event_result: List[StopEventResultStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopEventResult",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
