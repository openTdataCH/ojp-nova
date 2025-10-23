from dataclasses import dataclass
from ojp.ojpmulti_point_trip_delivery_structure import OjpmultiPointTripDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpmultiPointTripDelivery(OjpmultiPointTripDeliveryStructure):
    class Meta:
        name = "OJPMultiPointTripDelivery"
        namespace = "http://www.vdv.de/ojp"
