from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class TpegLoc02DirectionTypeEnum(Enum):
    ALL_DIRECTIONS = "allDirections"
    ANTICLOCKWISE = "anticlockwise"
    BOTH_WAYS = "bothWays"
    CLOCKWISE = "clockwise"
    EAST_BOUND = "eastBound"
    INNER_RING = "innerRing"
    NORTH_BOUND = "northBound"
    NORTH_EAST_BOUND = "northEastBound"
    NORTH_WEST_BOUND = "northWestBound"
    OPPOSITE = "opposite"
    OUTER_RING = "outerRing"
    SOUTH_BOUND = "southBound"
    SOUTH_EAST_BOUND = "southEastBound"
    SOUTH_WEST_BOUND = "southWestBound"
    WEST_BOUND = "westBound"
    UNKNOWN = "unknown"
    OTHER = "other"
