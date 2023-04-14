from dataclasses import dataclass, field
from typing import List
from ojp.onward_call_structure import OnwardCallStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class OnwardCallsStructure:
    """
    Type for CALLing pattern for JOURNEY PATTERN.
    """
    onward_call: List[OnwardCallStructure] = field(
        default_factory=list,
        metadata={
            "name": "OnwardCall",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
