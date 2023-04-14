from dataclasses import dataclass
from ojp.ojpfare_delivery_structure import OjpfareDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpfareDelivery(OjpfareDeliveryStructure):
    class Meta:
        name = "OJPFareDelivery"
        namespace = "http://www.vdv.de/ojp"
