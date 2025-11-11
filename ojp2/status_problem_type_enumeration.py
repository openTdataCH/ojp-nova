from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class StatusProblemTypeEnumeration(Enum):
    """
    Types of problems that may be returned in responses to status requests.

    :cvar STATUS_INSTANCE_USAGE_DEPRECATED: Usage of this instance is
        deprecated. Contact the provider for more information.
    :cvar STATUS_OTHER: A problem has occurred that does not have a
        specific problem type.
    """

    STATUS_INSTANCE_USAGE_DEPRECATED = "STATUS_INSTANCE_USAGE_DEPRECATED"
    STATUS_OTHER = "STATUS_OTHER"
