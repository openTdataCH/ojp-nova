from dataclasses import dataclass

from ojp2.ojpline_information_request_structure import (
    OjplineInformationRequestStructure,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjplineInformationRequest(OjplineInformationRequestStructure):
    """The service provides route information about a given LINE.

    This helps when displaying the LINE on maps. This implements a small
    part of model PI QR Schedule Request of TM 6.
    """

    class Meta:
        name = "OJPLineInformationRequest"
        namespace = "http://www.vdv.de/ojp"
