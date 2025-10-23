from dataclasses import dataclass
from ojp.ojpstatus_request_structure import OjpstatusRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstatusRequest(OjpstatusRequestStructure):
    class Meta:
        name = "OJPStatusRequest"
        namespace = "http://www.vdv.de/ojp"
