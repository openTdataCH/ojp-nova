from dataclasses import dataclass
from ojp.ojpavailability_request_structure import OjpavailabilityRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpavailabilityRequest(OjpavailabilityRequestStructure):
    class Meta:
        name = "OJPAvailabilityRequest"
        namespace = "http://www.vdv.de/ojp"
