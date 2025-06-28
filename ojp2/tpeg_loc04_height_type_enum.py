from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class TpegLoc04HeightTypeEnum(Enum):
    ABOVE = "above"
    ABOVE_SEA_LEVEL = "aboveSeaLevel"
    ABOVE_STREET_LEVEL = "aboveStreetLevel"
    AT = "at"
    AT_SEA_LEVEL = "atSeaLevel"
    AT_STREET_LEVEL = "atStreetLevel"
    BELOW = "below"
    BELOW_SEA_LEVEL = "belowSeaLevel"
    BELOW_STREET_LEVEL = "belowStreetLevel"
    UNDEFINED = "undefined"
    UNKNOWN = "unknown"
    OTHER = "other"
