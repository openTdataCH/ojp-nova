from dataclasses import dataclass

from ojp2.ojpstop_event_request_structure import OjpstopEventRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstopEventRequest(OjpstopEventRequestStructure):
    """This service provides information on arrivals and/or departures of public
    transport services from stops for a requested time or period of time.

    Restrictions can be set in the request parameters that filter the
    result contents accordingly. This service implements the model PI QR
    Stop Event Request from TM 6
    """

    class Meta:
        name = "OJPStopEventRequest"
        namespace = "http://www.vdv.de/ojp"
