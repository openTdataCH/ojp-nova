from dataclasses import dataclass
from ojp.ojpfare_request_structure import OjpfareRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpfareRequest(OjpfareRequestStructure):
    class Meta:
        name = "OJPFareRequest"
        namespace = "http://www.vdv.de/ojp"
