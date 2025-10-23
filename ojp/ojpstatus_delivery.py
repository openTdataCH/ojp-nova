from dataclasses import dataclass
from ojp.ojpstatus_delivery_structure import OjpstatusDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstatusDelivery(OjpstatusDeliveryStructure):
    class Meta:
        name = "OJPStatusDelivery"
        namespace = "http://www.vdv.de/ojp"
