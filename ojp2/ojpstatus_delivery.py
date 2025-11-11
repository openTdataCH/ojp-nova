from dataclasses import dataclass

from ojp2.ojpstatus_delivery_structure import OjpstatusDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstatusDelivery(OjpstatusDeliveryStructure):
    """
    The status service provides basic information about the operational status of
    an OJP system.
    """

    class Meta:
        name = "OJPStatusDelivery"
        namespace = "http://www.vdv.de/ojp"
