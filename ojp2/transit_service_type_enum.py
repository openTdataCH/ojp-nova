from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class TransitServiceTypeEnum(Enum):
    AIR = "air"
    BUS = "bus"
    FERRY = "ferry"
    HYDROFOIL = "hydrofoil"
    RAIL = "rail"
    TRAM = "tram"
    UNDERGROUND_METRO = "undergroundMetro"
