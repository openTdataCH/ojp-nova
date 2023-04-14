from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class AbnormalTrafficTypeEnum(Enum):
    STATIONARY_TRAFFIC = "stationaryTraffic"
    QUEUING_TRAFFIC = "queuingTraffic"
    SLOW_TRAFFIC = "slowTraffic"
    HEAVY_TRAFFIC = "heavyTraffic"
    UNSPECIFIED_ABNORMAL_TRAFFIC = "unspecifiedAbnormalTraffic"
    OTHER = "other"
