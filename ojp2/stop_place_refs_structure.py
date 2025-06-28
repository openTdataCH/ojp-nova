from dataclasses import dataclass, field

from ojp2.stop_place_ref_1 import StopPlaceRef1

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class StopPlaceRefsStructure:
    """
    Type for a collection of one or more references to a STOP PLACE.
    """

    stop_place_ref: list[StopPlaceRef1] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        },
    )
