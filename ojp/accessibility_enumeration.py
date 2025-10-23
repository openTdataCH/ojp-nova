from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


class AccessibilityEnumeration(Enum):
    """
    Enumeration of values for an accessibility value.
    """
    UNKNOWN = "unknown"
    FALSE = "false"
    TRUE = "true"
