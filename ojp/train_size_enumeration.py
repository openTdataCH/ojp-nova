from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TrainSizeEnumeration(Enum):
    """Allowed values for TRAIN SIZE.

    (since SIRI 2.1)
    """
    NORMAL = "normal"
    SHORT = "short"
    LONG = "long"
