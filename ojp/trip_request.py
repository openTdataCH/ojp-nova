from dataclasses import dataclass
from ojp.trip_request_structure import TripRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripRequest(TripRequestStructure):
    """
    Trip request element.
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"
