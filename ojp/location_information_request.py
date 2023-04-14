from dataclasses import dataclass
from ojp.location_information_request_structure import LocationInformationRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class LocationInformationRequest(LocationInformationRequestStructure):
    class Meta:
        namespace = "http://www.vdv.de/ojp"
