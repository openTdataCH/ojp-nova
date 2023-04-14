from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class EndTimeStatusEnumeration(Enum):
    """
    Allowed values for EndTime Status.
    """
    UNDEFINED = "undefined"
    LONG_TERM = "longTerm"
    SHORT_TERM = "shortTerm"
