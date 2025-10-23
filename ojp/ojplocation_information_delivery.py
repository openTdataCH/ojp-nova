from dataclasses import dataclass
from ojp.ojplocation_information_delivery_structure import OjplocationInformationDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjplocationInformationDelivery(OjplocationInformationDeliveryStructure):
    class Meta:
        name = "OJPLocationInformationDelivery"
        namespace = "http://www.vdv.de/ojp"
