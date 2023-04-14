from dataclasses import dataclass, field
from typing import List
from ojp.location_structure import LocationStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class AreaStructure:
    """
    Area described as a polygon.

    :ivar points: Ordered list of geographic locations describing the
        polygon of the area.
    """
    points: List[LocationStructure] = field(
        default_factory=list,
        metadata={
            "name": "Points",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 3,
        }
    )
