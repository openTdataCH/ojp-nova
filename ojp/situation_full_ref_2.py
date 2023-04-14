from dataclasses import dataclass
from ojp.situation_full_ref_structure_2 import SituationFullRefStructure2

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class SituationFullRef2(SituationFullRefStructure2):
    """Reference to situation message.

    Message details might be found in response context or through other
    communication channels.
    """
    class Meta:
        name = "SituationFullRef"
        namespace = "http://www.vdv.de/ojp"
