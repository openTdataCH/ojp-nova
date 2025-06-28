from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class PerspectiveEnumeration(Enum):
    """
    Values for perspectives.
    """

    GENERAL = "general"
    STOP_POINT = "stopPoint"
    VEHICLE_JOURNEY = "vehicleJourney"
