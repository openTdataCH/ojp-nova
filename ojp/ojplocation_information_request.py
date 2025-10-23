from dataclasses import dataclass
from ojp.ojplocation_information_request_structure import OjplocationInformationRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjplocationInformationRequest(OjplocationInformationRequestStructure):
    class Meta:
        name = "OJPLocationInformationRequest"
        namespace = "http://www.vdv.de/ojp"
