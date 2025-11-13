from dataclasses import dataclass

from ojp2.ojpstop_event_delivery_structure import OjpstopEventDeliveryStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstopEventDelivery(OjpstopEventDeliveryStructure):
    """This service provides information on arrivals and/or departures of public
    transport services from stops for a requested time or period of time.

    Restrictions can be set in the request parameters that filter the
    result contents accordingly. This service implements PI QR Stop
    Event Request from TM 6
    """

    class Meta:
        name = "OJPStopEventDelivery"
        namespace = "http://www.vdv.de/ojp"
