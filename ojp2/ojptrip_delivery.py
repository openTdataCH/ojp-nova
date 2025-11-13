from dataclasses import dataclass

from ojp2.ojptrip_delivery_structure import OjptripDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjptripDelivery(OjptripDeliveryStructure):
    """This service provides intermodal trip information from an origin location to
    a destination taking various user preferences into account.

    In the case of OJPTripRequest it is single origin and a single
    destination that are searched. This service implements the model PI
    QR Trip Request from TM 6.
    """

    class Meta:
        name = "OJPTripDelivery"
        namespace = "http://www.vdv.de/ojp"
