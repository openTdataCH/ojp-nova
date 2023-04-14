from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from ojp.mode_structure import ModeStructure
from ojp.place_structure import PlaceStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ExchangePointsResultStructure:
    """
    :ivar place: Place object that describes this exchange point.
    :ivar travel_duration_estimate: Rough estimate of the travel
        duration from the specified location to this exchange point.
    :ivar border_point: Flag if this exchange point is an administrative
        border point where timetables are cut off while services still
        may run through and connect the regions. At this kind of points
        passengers may continue their journey within the same service.
        Default is FALSE.
    :ivar mode: List of transport modes that call at this location
        object. This list should only be filled in case of stop points
        or stop places – and only when explicitly requested.
    """
    place: Optional[PlaceStructure] = field(
        default=None,
        metadata={
            "name": "Place",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    travel_duration_estimate: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TravelDurationEstimate",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    border_point: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BorderPoint",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    mode: List[ModeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
