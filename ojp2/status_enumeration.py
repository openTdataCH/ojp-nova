from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class StatusEnumeration(Enum):
    """Indicates whether the entity this annotates is available for use.

    Use of this attribute allows entities to be retired without deleting
    the details from the dataset.

    :cvar ACTIVE: Entity is active.
    :cvar INACTIVE: Entity is inactive.
    :cvar PENDING: Entity is still active but is in the process of being
        made inactive.
    """

    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"
