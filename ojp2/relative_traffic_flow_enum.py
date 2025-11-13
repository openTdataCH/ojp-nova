from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class RelativeTrafficFlowEnum(Enum):
    TRAFFIC_VERY_MUCH_HEAVIER_THAN_NORMAL = "trafficVeryMuchHeavierThanNormal"
    TRAFFIC_HEAVIER_THAN_NORMAL = "trafficHeavierThanNormal"
    TRAFFIC_FLOW_NORMAL = "trafficFlowNormal"
    TRAFFIC_LIGHTER_THAN_NORMAL = "trafficLighterThanNormal"
    TRAFFIC_VERY_MUCH_LIGHTER_THAN_NORMAL = "trafficVeryMuchLighterThanNormal"
