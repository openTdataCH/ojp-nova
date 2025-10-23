from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ConnectionDirectionEnumeration(Enum):
    """
    Values for DIRECTION of CONNECTION link or SERVCIE JOURNEY INTERCHANGE.
    """
    TO = "to"
    FROM = "from"
    BOTH = "both"
