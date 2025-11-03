from dataclasses import dataclass

from ojp2.ojpstatus_request_structure import OjpstatusRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstatusRequest(OjpstatusRequestStructure):
    """
    The status service provides basic information about the operational status of
    an OJP system.
    """

    class Meta:
        name = "OJPStatusRequest"
        namespace = "http://www.vdv.de/ojp"
