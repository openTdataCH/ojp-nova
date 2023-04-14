from dataclasses import dataclass
from ojp.ojptrip_refine_delivery_structure import OjptripRefineDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripRefineDelivery(OjptripRefineDeliveryStructure):
    class Meta:
        name = "OJPTripRefineDelivery"
        namespace = "http://www.vdv.de/ojp"
