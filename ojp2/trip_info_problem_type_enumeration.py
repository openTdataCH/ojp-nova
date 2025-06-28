from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class TripInfoProblemTypeEnumeration(Enum):
    """
    Types of problems that may be returned in responses to TripInfo requests.

    :cvar TRIPINFO_JOURNEYREFUNKNOWN: The journey reference used in the
        request is unknown.
    :cvar TRIPINFO_VEHICLEUNKNOWN: The vehicle reference used in the
        request is unknown.
    :cvar TRIPINFO_NOJOURNEYFOUND: No matching journey could be found
        for the requested time and journey/vehicle identifiers.
    :cvar TRIPINFO_NOGEOINFO: No geographic information available for
        this vehicle journey.
    :cvar TRIPINFO_NOREALTIME: No real-time information available.
    :cvar TRIPINFO_OTHER: A problem has occurred that does not have a
        specific problem type.
    """

    TRIPINFO_JOURNEYREFUNKNOWN = "TRIPINFO_JOURNEYREFUNKNOWN"
    TRIPINFO_VEHICLEUNKNOWN = "TRIPINFO_VEHICLEUNKNOWN"
    TRIPINFO_NOJOURNEYFOUND = "TRIPINFO_NOJOURNEYFOUND"
    TRIPINFO_NOGEOINFO = "TRIPINFO_NOGEOINFO"
    TRIPINFO_NOREALTIME = "TRIPINFO_NOREALTIME"
    TRIPINFO_OTHER = "TRIPINFO_OTHER"
