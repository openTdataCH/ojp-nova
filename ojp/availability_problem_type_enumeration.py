from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class AvailabilityProblemTypeEnumeration(Enum):
    """
    Types of problems that may be returned in responses to AVAILABILITY
    requests.

    :cvar AVAILABILITY_NOSERVICEFOUND: No SERVICE (VEHICLE JOURNEY or
        VEHICLE) could be found for this request.
    :cvar AVAILABILITY_LOCATIONUNSERVED: At the locations (address,
        stop, etc.) for which the availability has been requested, there
        is no public transport service at all. E.g. outside of the area.
    :cvar AVAILABILITY_LOCATIONUNKNOWN: The location (address, stop,
        etc.) for which availability was requested is unknown.
    :cvar AVAILABILITY_OUTSIDERULES: The vehicle is not available due to
        existing rules like operating hours or not competing against an
        existing public transport line. In the details of the problem
        there should be information indicating which rules were
        violated: e.g. The desired MOBILITY SERVICE can't be provided
        because there exists a regulare line for this TRIP.
    :cvar AVAILABILITY_SERVICEDISRUPTED: The MOBILITY SERVICE is
        disrupted.
    :cvar AVAILABILITY_UNAVAILABLE: There is no VEHICLE available at the
        current time.
    :cvar AVAILABILITY_OTHER: A problem has occurred that does not have
        a specific problem type.
    """
    AVAILABILITY_NOSERVICEFOUND = "AVAILABILITY_NOSERVICEFOUND"
    AVAILABILITY_LOCATIONUNSERVED = "AVAILABILITY_LOCATIONUNSERVED"
    AVAILABILITY_LOCATIONUNKNOWN = "AVAILABILITY_LOCATIONUNKNOWN"
    AVAILABILITY_OUTSIDERULES = "AVAILABILITY_OUTSIDERULES"
    AVAILABILITY_SERVICEDISRUPTED = "AVAILABILITY_SERVICEDISRUPTED"
    AVAILABILITY_UNAVAILABLE = "AVAILABILITY_UNAVAILABLE"
    AVAILABILITY_OTHER = "AVAILABILITY_OTHER"
