from dataclasses import dataclass
from ojp.ojptrip_info_request_structure import OjptripInfoRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripInfoRequest(OjptripInfoRequestStructure):
    class Meta:
        name = "OJPTripInfoRequest"
        namespace = "http://www.vdv.de/ojp"
