from dataclasses import dataclass, field

from ojp2.place_structure import PlaceStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PlacesStructure:
    """
    Structure providing a collection of places.
    """

    place: list[PlaceStructure] = field(
        default_factory=list,
        metadata={
            "name": "Place",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
