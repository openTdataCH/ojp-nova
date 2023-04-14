from dataclasses import dataclass, field
from typing import List
from ojp.location_structure import LocationStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class LinearShapeStructure:
    """An oriented correspondence from one LINK or ROUTE of a source layer,
    onto an entity in a target layer: e.g. LINK SEQUENCE.

    As OJP is reduced in relation to NeTEx, we use a simple general
    structure.

    :ivar position: Ordered list of locations representing the geometry
        of the link or route.
    """
    position: List[LocationStructure] = field(
        default_factory=list,
        metadata={
            "name": "Position",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 2,
        }
    )
