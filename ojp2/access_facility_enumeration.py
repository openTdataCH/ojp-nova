from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class AccessFacilityEnumeration(Enum):
    """
    Values for Access Facility.
    """

    UNKNOWN = "unknown"
    LIFT = "lift"
    ESCALATOR = "escalator"
    TRAVELATOR = "travelator"
    RAMP = "ramp"
    STAIRS = "stairs"
    SHUTTLE = "shuttle"
    NARROW_ENTRANCE = "narrowEntrance"
    BARRIER = "barrier"
    PALLET_ACCESS_LOW_FLOOR = "palletAccess_lowFloor"
    VALIDATOR = "validator"
