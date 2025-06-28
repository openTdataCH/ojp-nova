from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


class ProbabilityOfOccurrenceEnum(Enum):
    CERTAIN = "certain"
    PROBABLE = "probable"
    RISK_OF = "riskOf"
