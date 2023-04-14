from dataclasses import dataclass, field
from typing import Optional
from ojp.stop_event_problem_type_enumeration import StopEventProblemTypeEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopEventProblemType:
    class Meta:
        namespace = "http://www.vdv.de/ojp"

    value: Optional[StopEventProblemTypeEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
