from dataclasses import dataclass, field
from typing import Optional

from ojp2.ojperror_structure import OjperrorStructure
from ojp2.stop_event_structure import StopEventStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopEventResultStructure:
    """
    Wrapper element for a single stop event result.

    :ivar id: ID of this result.
    :ivar error_condition: Problems related to this STOPEVENT result.
    :ivar stop_event: Stop event data element.
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
    stop_event: Optional[StopEventStructure] = field(
        default=None,
        metadata={
            "name": "StopEvent",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
