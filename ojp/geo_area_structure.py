from dataclasses import dataclass, field
from typing import List
from ojp.location_structure import LocationStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class GeoAreaStructure:
    """
    [specialisation of ZONE in TMv6] a LINK SEQUENCE (one-dimensional) forming the
    boundary of a ZONE.
    """
    polyline_point: List[LocationStructure] = field(
        default_factory=list,
        metadata={
            "name": "PolylinePoint",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 3,
        }
    )
