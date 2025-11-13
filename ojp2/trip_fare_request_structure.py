from dataclasses import dataclass, field
from typing import Optional

from ojp2.response_context_structure import ResponseContextStructure
from ojp2.trip_structure import TripStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripFareRequestStructure:
    """
    Structure of a Single Trip Fare Request.

    :ivar trip_context: Context to hold trip related objects that occur
        frequently. Especially necessary, when the system answering the
        fare request is not the same as the one that did the trip
        request.
    :ivar trip: A complete trip from origin to destination
    """

    trip_context: Optional[ResponseContextStructure] = field(
        default=None,
        metadata={
            "name": "TripContext",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    trip: Optional[TripStructure] = field(
        default=None,
        metadata={
            "name": "Trip",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
