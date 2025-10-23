from dataclasses import dataclass, field
from typing import List
from ojp.trip_structure import TripStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class MultiTripFareRequestStructure:
    """
    Structure of a Multi Trip Fare Request.

    :ivar trip: Multiple complete trips from multiple origins and
        multiple destination
    """
    trip: List[TripStructure] = field(
        default_factory=list,
        metadata={
            "name": "Trip",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        }
    )
