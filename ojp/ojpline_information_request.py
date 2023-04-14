from dataclasses import dataclass
from ojp.ojpline_information_request_structure import OjplineInformationRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjplineInformationRequest(OjplineInformationRequestStructure):
    class Meta:
        name = "OJPLineInformationRequest"
        namespace = "http://www.vdv.de/ojp"
