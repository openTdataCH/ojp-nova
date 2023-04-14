from dataclasses import dataclass, field
from typing import List
from ojp.previous_call_structure import PreviousCallStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PreviousCallsStructure:
    """
    Type for Ordered list of CALLs at previous stop.
    """
    previous_call: List[PreviousCallStructure] = field(
        default_factory=list,
        metadata={
            "name": "PreviousCall",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
