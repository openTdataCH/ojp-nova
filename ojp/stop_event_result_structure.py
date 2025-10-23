from dataclasses import dataclass, field
from typing import List, Optional
from ojp.error_message_structure import ErrorMessageStructure
from ojp.stop_event_structure import StopEventStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopEventResultStructure:
    """
    Wrapper element for a single stop event result.

    :ivar result_id: ID of this result.
    :ivar error_message: Error messages that refer to this stop event.
    :ivar stop_event: Stop event data element.
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
    stop_event: Optional[StopEventStructure] = field(
        default=None,
        metadata={
            "name": "StopEvent",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
