from dataclasses import dataclass
from ojp.ojpavailability_delivery_structure import OjpavailabilityDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpavailabilityDelivery(OjpavailabilityDeliveryStructure):
    class Meta:
        name = "OJPAvailabilityDelivery"
        namespace = "http://www.vdv.de/ojp"
