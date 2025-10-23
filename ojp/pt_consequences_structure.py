from dataclasses import dataclass, field
from typing import List
from ojp.pt_consequence_structure import PtConsequenceStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PtConsequencesStructure:
    """
    Type for list of effects.

    :ivar consequence: Nature of the effect to disrupt (or restore)
        service, and further details.
    """
    consequence: List[PtConsequenceStructure] = field(
        default_factory=list,
        metadata={
            "name": "Consequence",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
