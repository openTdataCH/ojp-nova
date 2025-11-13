from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class PredictabilityEnumeration(Enum):
    """
    Values for Predictability Status.
    """

    PLANNED = "planned"
    UNPLANNED = "unplanned"
    ALL = "all"
