from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class ComparisonOperatorEnum(Enum):
    EQUAL_TO = "equalTo"
    GREATER_THAN = "greaterThan"
    GREATHER_THAN_OR_EQUAL_TO = "greatherThanOrEqualTo"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL_TO = "lessThanOrEqualTo"
