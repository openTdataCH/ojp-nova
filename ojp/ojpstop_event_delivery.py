from dataclasses import dataclass
from ojp.ojpstop_event_delivery_structure import OjpstopEventDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstopEventDelivery(OjpstopEventDeliveryStructure):
    class Meta:
        name = "OJPStopEventDelivery"
        namespace = "http://www.vdv.de/ojp"
