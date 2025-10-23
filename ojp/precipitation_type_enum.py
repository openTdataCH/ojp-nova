from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class PrecipitationTypeEnum(Enum):
    DRIZZLE = "drizzle"
    FREEZING_RAIN = "freezingRain"
    HAIL = "hail"
    RAIN = "rain"
    SLEET = "sleet"
    SNOW = "snow"
