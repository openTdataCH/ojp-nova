from dataclasses import dataclass
from ojp.pt_situation_element_structure import PtSituationElementStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PtSituationElement(PtSituationElementStructure):
    """
    Type for individual IPT ncident.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
