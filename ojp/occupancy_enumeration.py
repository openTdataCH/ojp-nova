from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class OccupancyEnumeration(Enum):
    """
    Passenger load status of a VEHICLE.
    """
    FULL = "full"
    SEATS_AVAILABLE = "seatsAvailable"
    STANDING_AVAILABLE = "standingAvailable"
