from dataclasses import dataclass, field
from typing import Optional
from ojp.situation_full_ref_1 import SituationFullRef1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SituationRefStructure:
    """
    Type for reference to a SITUATION.

    :ivar situation_simple_ref:
    :ivar situation_full_ref: Reference to a SITUATION. Elements of
        SITUATION identfier are expressed as atomic elements.
    """
    situation_simple_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SituationSimpleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    situation_full_ref: Optional[SituationFullRef1] = field(
        default=None,
        metadata={
            "name": "SituationFullRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
