from dataclasses import dataclass
from ojp.ojptrip_delivery_structure import OjptripDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripDelivery(OjptripDeliveryStructure):
    class Meta:
        name = "OJPTripDelivery"
        namespace = "http://www.vdv.de/ojp"
