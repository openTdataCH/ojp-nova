from dataclasses import dataclass

from ojp2.ojpstatus_response_structure import OjpstatusResponseStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstatusResponse(OjpstatusResponseStructure):
    class Meta:
        name = "OJPStatusResponse"
        namespace = "http://www.vdv.de/ojp"
