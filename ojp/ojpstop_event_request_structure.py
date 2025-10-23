from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_ojpservice_request_structure import AbstractOjpserviceRequestStructure
from ojp.extensions_1 import Extensions1
from ojp.place_context_structure import PlaceContextStructure
from ojp.stop_event_param_structure import StopEventParamStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OjpstopEventRequestStructure(AbstractOjpserviceRequestStructure):
    """
    :ivar location: Location for which to obtain stop event information.
    :ivar params: Request parameter
    :ivar extensions:
    """
    class Meta:
        name = "OJPStopEventRequestStructure"

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
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
