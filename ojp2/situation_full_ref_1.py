from dataclasses import dataclass

from ojp2.situation_full_ref_structure_1 import SituationFullRefStructure1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SituationFullRef1(SituationFullRefStructure1):
    """Reference to a SITUATION.

    Elements are retained as atomic elements.
    """

    class Meta:
        name = "SituationFullRef"
        namespace = "http://www.siri.org.uk/siri"
