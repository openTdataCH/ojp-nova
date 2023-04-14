from dataclasses import dataclass
from ojp.ojpmulti_point_trip_request_structure import OjpmultiPointTripRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpmultiPointTripRequest(OjpmultiPointTripRequestStructure):
    class Meta:
        name = "OJPMultiPointTripRequest"
        namespace = "http://www.vdv.de/ojp"
