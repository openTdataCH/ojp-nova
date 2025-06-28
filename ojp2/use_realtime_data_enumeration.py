from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class UseRealtimeDataEnumeration(Enum):
    """
    :cvar FULL: Full use of real-time information, including removal of
        SERVICE JOURNEYS (TRIP REQUEST POLICY.UseRealTime is only a
        boolean in Transmodel).
    :cvar EXPLANATORY: Cancelled and delayed SERVICE JOURNEYs are still
        returned, but an additional explanatory textual information is
        provided to describe their current real-time status.
    :cvar NONE: Only based on timetable data
    """

    FULL = "full"
    EXPLANATORY = "explanatory"
    NONE = "none"
