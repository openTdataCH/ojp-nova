from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class ValidityStatusEnum(Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    DEFINED_BY_VALIDITY_TIME_SPEC = "definedByValidityTimeSpec"
