from dataclasses import dataclass
from ojp.trip_response_structure import TripResponseStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripResponse(TripResponseStructure):
    """
    Trip response element.
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"
