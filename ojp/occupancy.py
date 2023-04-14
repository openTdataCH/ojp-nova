from dataclasses import dataclass, field
from typing import Optional
from ojp.occupancy_enumeration import OccupancyEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class Occupancy:
    """An approximate figure of how occupied the journey is after departing
    from a given stop, e.g. 'manySeatsAvailable' or 'standingRoomOnly'.

    If omitted: Passenger load is unknown. Occupancies and capacities
    for individual VEHICLEs, e.g. parts of a COMPOUND TRAIN, can also be
    specified in more detail for the departure on CALL level.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[OccupancyEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
