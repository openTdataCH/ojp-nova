from dataclasses import dataclass, field
from typing import Optional
from ojp.trip_structure import TripStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripFareRequestStructure:
    """
    Structure of a Single Trip Fare Request.

    :ivar trip: A complete trip from origin to destination
    """
    trip: Optional[TripStructure] = field(
        default=None,
        metadata={
            "name": "Trip",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
