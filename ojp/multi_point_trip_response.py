from dataclasses import dataclass
from ojp.multi_point_trip_response_structure import MultiPointTripResponseStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class MultiPointTripResponse(MultiPointTripResponseStructure):
    """
    Multi-point trip response element.
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"
