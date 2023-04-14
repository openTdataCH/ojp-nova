from dataclasses import dataclass
from ojp.location_information_response_structure import LocationInformationResponseStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class LocationInformationResponse(LocationInformationResponseStructure):
    class Meta:
        namespace = "http://www.vdv.de/ojp"
