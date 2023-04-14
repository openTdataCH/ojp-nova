from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from ojp.call_at_stop_structure import CallAtStopStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class CallAtNearStopStructure:
    """
    indication of the walk distance and time to a nearby stop where relevant.

    :ivar call_at_stop: [same as CALL in SIRI] the meeting of a VEHICLE
        JOURNEY with a specific SCHEDULED STOP POINT .
    :ivar walk_distance: Distance from request location (f.e. address)
        to this stop in metres.
    :ivar walk_duration: Distance from request location (f.e. address)
        to this stop in seconds. All user options taken into account
        (f.e. walk speed).
    """
    call_at_stop: Optional[CallAtStopStructure] = field(
        default=None,
        metadata={
            "name": "CallAtStop",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    walk_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "WalkDistance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    walk_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "WalkDuration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
