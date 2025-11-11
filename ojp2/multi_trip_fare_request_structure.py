from dataclasses import dataclass, field
from typing import Optional

from ojp2.response_context_structure import ResponseContextStructure
from ojp2.trip_structure import TripStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class MultiTripFareRequestStructure:
    """
    Structure of a Multi Trip Fare Request.

    :ivar trip_context: Context to hold trip related objects that occur
        frequently.
    :ivar trip: Multiple complete trips from multiple origins and
        multiple destination
    """

    trip_context: Optional[ResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "TripContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip: list[TripStructure] = field(
        default_factory=list,
        metadata={
            "name": "Trip",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
