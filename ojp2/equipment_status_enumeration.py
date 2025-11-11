from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class EquipmentStatusEnumeration(Enum):
    """
    Availabilityload status of a EQUIPMENT.
    """

    UNKNOWN = "unknown"
    AVAILABLE = "available"
    NOT_AVAILABLE = "notAvailable"
