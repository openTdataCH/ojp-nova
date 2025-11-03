from dataclasses import dataclass, field

from ojp2.pt_situation_element_structure import PtSituationElementStructure
from ojp2.road_situation_element_structure import RoadSituationElementStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class SituationsStructure:
    """
    Wrapper type for SIRI PtSituationsElementStructure.

    :ivar pt_situation: SIRI situation details in public transport, see
        CEN/TS 15531-5.
    :ivar road_situation: SIRI situation details in individual
        transport, see CEN/TS 15531-5.
    """

    pt_situation: list[PtSituationElementStructure] = field(
        default_factory=list,
        metadata={
            "name": "PtSituation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    road_situation: list[RoadSituationElementStructure] = field(
        default_factory=list,
        metadata={
            "name": "RoadSituation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
