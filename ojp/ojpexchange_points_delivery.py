from dataclasses import dataclass
from ojp.ojpexchange_points_delivery_structure import OjpexchangePointsDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpexchangePointsDelivery(OjpexchangePointsDeliveryStructure):
    class Meta:
        name = "OJPExchangePointsDelivery"
        namespace = "http://www.vdv.de/ojp"
