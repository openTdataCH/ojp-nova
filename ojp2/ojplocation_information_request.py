from dataclasses import dataclass

from ojp2.ojplocation_information_request_structure import (
    OjplocationInformationRequestStructure,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjplocationInformationRequest(OjplocationInformationRequestStructure):
    """The Location Information service comprises the following four base functions:
    matching text input against possible origin and destination locations, retrieval of all location objects (bunch delivery), geographical context service that provides location objects within a bounding box, reverse address resolution service that delivers the nearest address for a given coordinate.
    By means of abstraction these functions are assembled within one single service – the Location Information service. This way, even more possible applications have arisen, such as: finding the nearest stops/stations for a given coordinate, matching text input against the names of locations near a given coordinate. This service implements the model PI QR Location Request from TM 6."""

    class Meta:
        name = "OJPLocationInformationRequest"
        namespace = "http://www.vdv.de/ojp"
