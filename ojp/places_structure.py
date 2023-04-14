from dataclasses import dataclass, field
from typing import List
from ojp.place_structure import PlaceStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PlacesStructure:
    """
    Structure providing a collection of places.
    """
    place: List[PlaceStructure] = field(
        default_factory=list,
        metadata={
            "name": "Place",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
