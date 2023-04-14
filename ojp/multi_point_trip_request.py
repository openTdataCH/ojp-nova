from dataclasses import dataclass
from ojp.multi_point_trip_request_structure import MultiPointTripRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class MultiPointTripRequest(MultiPointTripRequestStructure):
    class Meta:
        namespace = "http://www.vdv.de/ojp"
