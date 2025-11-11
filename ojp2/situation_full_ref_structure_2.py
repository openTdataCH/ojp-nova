from dataclasses import dataclass

from ojp2.situation_full_ref_structure_1 import SituationFullRefStructure1

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class SituationFullRefStructure2(SituationFullRefStructure1):
    """Reference structure for situation message.

    Situation details might be found in response context or through
    other communication channels.
    """

    class Meta:
        name = "SituationFullRefStructure"
