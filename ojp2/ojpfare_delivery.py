from dataclasses import dataclass

from ojp2.ojpfare_delivery_structure import OjpfareDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpfareDelivery(OjpfareDeliveryStructure):
    """This service provides general, stop-specific and trip-specific fare
    information.

    This service implements the models PI Stop Fare Request, PI FQ Fare
    Product Request, PI FQ Single Trip Fare Request from TM 6.
    """

    class Meta:
        name = "OJPFareDelivery"
        namespace = "http://www.vdv.de/ojp"
