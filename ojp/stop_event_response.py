from dataclasses import dataclass
from ojp.stop_event_response_structure import StopEventResponseStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopEventResponse(StopEventResponseStructure):
    """
    Response element for departure and arrival events at stops.
    """
    class Meta:
        namespace = "http://www.vdv.de/ojp"
