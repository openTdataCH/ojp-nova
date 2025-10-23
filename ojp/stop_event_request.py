from dataclasses import dataclass
from ojp.stop_event_request_structure import StopEventRequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopEventRequest(StopEventRequestStructure):
    """
    Request element for departure and arrival events at stops.
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"
