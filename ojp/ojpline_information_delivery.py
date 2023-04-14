from dataclasses import dataclass
from ojp.ojpline_information_delivery_structure import OjplineInformationDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjplineInformationDelivery(OjplineInformationDeliveryStructure):
    class Meta:
        name = "OJPLineInformationDelivery"
        namespace = "http://www.vdv.de/ojp"
