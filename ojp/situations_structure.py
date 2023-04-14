from dataclasses import dataclass, field
from typing import List
from ojp.pt_situation_element_structure import PtSituationElementStructure
from ojp.road_situation_element_structure import RoadSituationElementStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class SituationsStructure:
    """
    Wrapper type for SIRI PtSituationsElementStructure.

    :ivar pt_situation: SIRI situation details.
    :ivar road_situation:
    """
    pt_situation: List[PtSituationElementStructure] = field(
        default_factory=list,
        metadata={
            "name": "PtSituation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    road_situation: List[RoadSituationElementStructure] = field(
        default_factory=list,
        metadata={
            "name": "RoadSituation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
