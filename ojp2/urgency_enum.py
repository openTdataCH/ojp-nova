from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class UrgencyEnum(Enum):
    EXTREMELY_URGENT = "extremelyUrgent"
    URGENT = "urgent"
    NORMAL_URGENCY = "normalUrgency"
