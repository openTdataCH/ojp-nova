from dataclasses import dataclass
from ojp.ojptrip_refine_request_structure import OjptripRefineRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripRefineRequest(OjptripRefineRequestStructure):
    class Meta:
        name = "OJPTripRefineRequest"
        namespace = "http://www.vdv.de/ojp"
