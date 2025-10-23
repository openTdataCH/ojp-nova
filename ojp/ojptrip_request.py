from dataclasses import dataclass
from ojp.ojptrip_request_structure import OjptripRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripRequest(OjptripRequestStructure):
    class Meta:
        name = "OJPTripRequest"
        namespace = "http://www.vdv.de/ojp"
