from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class StopEventProblemTypeEnumeration(Enum):
    """
    Types of problems that may be returned in responses to STOPEVENT requests.

    :cvar STOPEVENT_NOEVENTFOUND: No departure/arrival could be found
        within the requested period that meets the given restrictions.
    :cvar STOPEVENT_LOCATIONUNSERVED: At the locations (address, stop,
        etc.) for which stop events have been requested, there is no
        public transport service at all.
    :cvar STOPEVENT_LOCATIONUNKNOWN: The location (address, stop, etc.)
        for which stop events were requested is unknown.
    :cvar STOPEVENT_DATEOUTOFRANGE: There are no timetables available
        for the requested date.
    :cvar STOPEVENT_LASTSERVICEOFTHISLINE: This departure/arrival event
        is the last one of this line for this operating day.
    :cvar STOPEVENT_NOREALTIME: There is no real-time or forecast data
        available for this departure/arrival event.
    :cvar STOPEVENT_OTHER: A problem has occurred that does not have a
        specific problem type.
    """

    STOPEVENT_NOEVENTFOUND = "STOPEVENT_NOEVENTFOUND"
    STOPEVENT_LOCATIONUNSERVED = "STOPEVENT_LOCATIONUNSERVED"
    STOPEVENT_LOCATIONUNKNOWN = "STOPEVENT_LOCATIONUNKNOWN"
    STOPEVENT_DATEOUTOFRANGE = "STOPEVENT_DATEOUTOFRANGE"
    STOPEVENT_LASTSERVICEOFTHISLINE = "STOPEVENT_LASTSERVICEOFTHISLINE"
    STOPEVENT_NOREALTIME = "STOPEVENT_NOREALTIME"
    STOPEVENT_OTHER = "STOPEVENT_OTHER"
