from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class DirectionEnum(Enum):
    ANTICLOCKWISE = "anticlockwise"
    CLOCKWISE = "clockwise"
    NORTH_BOUND = "northBound"
    NORTH_EAST_BOUND = "northEastBound"
    EAST_BOUND = "eastBound"
    SOUTH_EAST_BOUND = "southEastBound"
    SOUTH_BOUND = "southBound"
    SOUTH_WEST_BOUND = "southWestBound"
    WEST_BOUND = "westBound"
    NORTH_WEST_BOUND = "northWestBound"
    INBOUND_TOWARDS_TOWN = "inboundTowardsTown"
    OUTBOUND_FROM_TOWN = "outboundFromTown"
