from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class RemedyTypeEnumeration(Enum):
    """
    Allowed values for actions to remedy a facility change.
    """

    UNKNOWN = "unknown"
    REPLACE = "replace"
    REPAIR = "repair"
    REMOVE = "remove"
    OTHER_ROUTE = "otherRoute"
    OTHER_LOCATION = "otherLocation"
