from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TypeOfNestedQuayEnumeration(Enum):
    """Allowed values for characterisation of nested QUAYs as part of a STOP
    ASSIGNMENT.

    (since SIRI 2.1)

    :cvar PLATFORM_GROUP: A type of QUAY that consists of multiple QUAYs
        of type 'platform'. Examples of such groups would be the lower
        and upper level of a station.
    :cvar PLATFORM: A type of QUAY that consists of at least two child
        QUAYs of type 'platformEdge'.
    :cvar PLATFORM_EDGE: A type of QUAY which allows direct access to a
        VEHICLE, e.g. an on-street bus stop, or consists of multiple
        child QUAYs of type 'platformSector'.
    :cvar PLATFORM_SECTOR: A QUAY of type 'platformEdge' may be divided
        into multiple sectors, e.g. "A", "B", "C" etc., to help
        passengers find a specific part of a vehicle. The first class
        carriage of a TRAIN might, for example, be assigned to sector
        "A" of a QUAY.
    """
    PLATFORM_GROUP = "platformGroup"
    PLATFORM = "platform"
    PLATFORM_EDGE = "platformEdge"
    PLATFORM_SECTOR = "platformSector"
