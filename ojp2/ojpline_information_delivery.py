from dataclasses import dataclass

from ojp2.ojpline_information_delivery_structure import (
    OjplineInformationDeliveryStructure,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjplineInformationDelivery(OjplineInformationDeliveryStructure):
    """The service provides route information about a given LINE.

    This helps when displaying the LINE on maps. This implements a small
    part of PI QR Schedule Request of TM 6.
    """

    class Meta:
        name = "OJPLineInformationDelivery"
        namespace = "http://www.vdv.de/ojp"
