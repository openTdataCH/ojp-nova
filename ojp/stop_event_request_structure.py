from dataclasses import dataclass, field
from typing import Optional
from ojp.place_context_structure import PlaceContextStructure
from ojp.stop_event_param_structure import StopEventParamStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopEventRequestStructure:
    """
    :ivar location: Location for which to obtain stop event information.
    :ivar params: Request parameter
    """
    location: Optional[PlaceContextStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    params: Optional[StopEventParamStructure] = field(
        default=None,
        metadata={
            "name": "Params",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
