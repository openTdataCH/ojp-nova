from dataclasses import dataclass
from ojp.ojptrip_info_delivery_structure import OjptripInfoDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripInfoDelivery(OjptripInfoDeliveryStructure):
    class Meta:
        name = "OJPTripInfoDelivery"
        namespace = "http://www.vdv.de/ojp"
