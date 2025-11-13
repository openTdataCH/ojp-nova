from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class TrafficTrendTypeEnum(Enum):
    TRAFFIC_BUILDING_UP = "trafficBuildingUp"
    TRAFFIC_EASING = "trafficEasing"
    TRAFFIC_STABLE = "trafficStable"
    UNKNOWN = "unknown"
