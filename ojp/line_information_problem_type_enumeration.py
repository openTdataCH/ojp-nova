from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class LineInformationProblemTypeEnumeration(Enum):
    """
    Types of problems that may be returned in responses to LINE INFORMATION
    requests.

    :cvar LINEINFORMATION_LINEUNKNOWN: The requested LINE is unknown.
    :cvar LINEINFORMATION_OTHER: A problem has occurred that does not
        have a specific problem type.
    """
    LINEINFORMATION_LINEUNKNOWN = "LINEINFORMATION_LINEUNKNOWN"
    LINEINFORMATION_OTHER = "LINEINFORMATION_OTHER"
