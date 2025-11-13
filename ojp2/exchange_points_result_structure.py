from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.mode_structure import ModeStructure
from ojp2.ojperror_structure import OjperrorStructure
from ojp2.place_structure import PlaceStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ExchangePointsResultStructure:
    """
    :ivar error_condition: Problems related to this EXCHANGE POINTS
        result.
    :ivar place: Place object that describes this exchange point.
    :ivar travel_duration_estimate: Rough estimate of the travel
        duration from the specified reference location/place to this
        exchange point.
    :ivar wait_duration: Duration needed at this exchange point to
        change from one service to another. If a journey planning
        orchestrator puts together a trip at this exchange point, it
        must take care, that feeding arrival and fetching departure are
        at least this duration apart.
    :ivar border_point: Flag if this exchange point is an administrative
        border point where timetables are cut off while services still
        may run through and connect the regions. At this kind of points
        passengers may continue their journey within the same service.
        Default is FALSE.
    :ivar mode: List of transport modes that call at this place object.
        This list should only be filled in case of stop points or stop
        places – and only when explicitly requested.
    :ivar priority: The priority of the exchange point. 100 is the
        maximum. The priority can be used to select given ExchangePoints
        more often (e.g., because the station is a main hub).
    """

    error_condition: list[OjperrorStructure] = field(
        default_factory=list,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    place: Optional[PlaceStructure] = field(
        default=None,
        metadata={
            "name": "Place",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    travel_duration_estimate: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "TravelDurationEstimate",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    wait_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "WaitDuration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    border_point: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BorderPoint",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    mode: list[ModeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "max_inclusive": 100,
        },
    )
