from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class StopPlaceRefsStructure:
    """
    Type for a collection of one or more references to a STOP PLACE.
    """
    stop_place_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "min_occurs": 1,
        }
    )
