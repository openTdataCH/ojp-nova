from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class ActionStatusEnumeration(Enum):
    """
    Values for Progress Status.
    """
    OPEN = "open"
    PUBLISHED = "published"
    CLOSED = "closed"
