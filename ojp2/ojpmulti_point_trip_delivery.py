from dataclasses import dataclass

from ojp2.ojpmulti_point_trip_delivery_structure import (
    OjpmultiPointTripDeliveryStructure,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpmultiPointTripDelivery(OjpmultiPointTripDeliveryStructure):
    """This service provides intermodal trip information from multiple origin
    location to multiple destination taking various user preferences into account.

    In the case of OJPMultipointTripRequest it is a set of origins and
    destinations that are searched. This service implements the model PI
    QR Trip Request from TM 6.
    """

    class Meta:
        name = "OJPMultiPointTripDelivery"
        namespace = "http://www.vdv.de/ojp"
