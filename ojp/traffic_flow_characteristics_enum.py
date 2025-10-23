from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class TrafficFlowCharacteristicsEnum(Enum):
    ERRATIC_FLOW = "erraticFlow"
    SMOOTH_FLOW = "smoothFlow"
    STOP_AND_GO = "stopAndGo"
    TRAFFIC_BLOCKED = "trafficBlocked"
