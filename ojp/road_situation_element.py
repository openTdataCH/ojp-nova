from dataclasses import dataclass
from ojp.road_situation_element_structure import RoadSituationElementStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RoadSituationElement(RoadSituationElementStructure):
    """
    Type for individual IPT ncident.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
