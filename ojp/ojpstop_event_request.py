from dataclasses import dataclass
from ojp.ojpstop_event_request_structure import OjpstopEventRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstopEventRequest(OjpstopEventRequestStructure):
    class Meta:
        name = "OJPStopEventRequest"
        namespace = "http://www.vdv.de/ojp"
