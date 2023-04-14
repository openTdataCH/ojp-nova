from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class TripProblemTypeEnumeration(Enum):
    """
    Types of problems that may be returned in responses to Trip requests.

    :cvar TRIP_NOTRIPFOUND: No trip plan could be found that meets all
        the parameters as they have been set by the user (start and end
        locations, departure/arrival time and further options possibly
        set by the user).
    :cvar TRIP_ORIGINUNKNOWN: The start location (address, stop place,
        …) for the requested trip is unknown.
    :cvar TRIP_DESTINATIONUNKNOWN: The end location (address, stop
        place, …) for the requested trip is unknown.
    :cvar TRIP_VIAUNKNOWN: One of the via points is unknown.
    :cvar TRIP_NOTVIAUNKNOWN: One of the not-via points is unknown.
    :cvar TRIP_NOCHANGEATUNKNOWN: One of the no-change-at stations is
        unknown.
    :cvar TRIP_NOORIGIN: No start location has been defined for the
        trip.
    :cvar TRIP_NODESTINATION: No end location has been defined for the
        trip.
    :cvar TRIP_ORIGINDESTINATIONIDENTICAL: Start and end of the trip are
        identical.
    :cvar TRIP_DATETIMEERROR: The requested date and/or time do not make
        sense.
    :cvar TRIP_DEPARTUREAFTERARRIVAL: The requested departure time at
        each origin is after the requested arrival time at any
        destination.
    :cvar TRIP_DATEOUTOFRANGE: There is no timetable data available for
        the requested date.
    :cvar TRIP_ORIGINEQUIVALENT: The requested origin stop place has
        been replaced by an equivalent stop place.
    :cvar TRIP_DESTINATIONEQUIVALENT: The requested destination stop
        place has been replaced by an equivalent stop place.
    :cvar TRIP_VIAEQUIVALENT: One of the requested via stop places has
        been replaced by an equivalent stop place.
    :cvar TRIP_REALTIMEINCOMPLETE: There is no realtime information
        available for at least one of the services within this trip
        result.
    :cvar TRIP_ITTIMEEXTENDED: The maximum time allowed for using modes
        of individual transport (mostly walking or cycling) has been
        extended by the system because otherwise no trip could be found.
    :cvar TRIP_ITMODECHANGED: The mode of individual transport specified
        by the user has been replaced by the system because otherwise no
        trip could be found. Usually this means taking a taxi instead of
        walking.
    :cvar TRIP_INCONVENIENTWAITING: The trip plan in this trip result
        contains a long waiting time.
    :cvar TRIP_MULTIPOINT_NOTALLPOINTSCOVERED: No trip solution was
        found covering each of the requested points.
    :cvar TRIP_MULTIPOINT_TOOMANYPOINTS: Too many points have been
        requested as departure or arrival.
    :cvar TRIP_MULTIPOINT_TYPE_NOT_SUPPORTED: The indicated multipoint
        type is not supported.
    :cvar TRIP_REFINE_LEG_UNKNOWN: Indicated legs do not exist.
    :cvar REFINE_OBJECTNOTFOUND: The object to be refined could not be
        found in the database of the responding system or could not be
        found unequivocally.
    :cvar REFINE_PROFILENOTSUPPORTED: Refinement does not support the
        hiking or cycling profile.
    :cvar TRIP_OTHER: A problem has occurred that does not have a
        specific problem type.
    """
    TRIP_NOTRIPFOUND = "TRIP_NOTRIPFOUND"
    TRIP_ORIGINUNKNOWN = "TRIP_ORIGINUNKNOWN"
    TRIP_DESTINATIONUNKNOWN = "TRIP_DESTINATIONUNKNOWN"
    TRIP_VIAUNKNOWN = "TRIP_VIAUNKNOWN"
    TRIP_NOTVIAUNKNOWN = "TRIP_NOTVIAUNKNOWN"
    TRIP_NOCHANGEATUNKNOWN = "TRIP_NOCHANGEATUNKNOWN"
    TRIP_NOORIGIN = "TRIP_NOORIGIN"
    TRIP_NODESTINATION = "TRIP_NODESTINATION"
    TRIP_ORIGINDESTINATIONIDENTICAL = "TRIP_ORIGINDESTINATIONIDENTICAL"
    TRIP_DATETIMEERROR = "TRIP_DATETIMEERROR"
    TRIP_DEPARTUREAFTERARRIVAL = "TRIP_DEPARTUREAFTERARRIVAL"
    TRIP_DATEOUTOFRANGE = "TRIP_DATEOUTOFRANGE"
    TRIP_ORIGINEQUIVALENT = "TRIP_ORIGINEQUIVALENT"
    TRIP_DESTINATIONEQUIVALENT = "TRIP_DESTINATIONEQUIVALENT"
    TRIP_VIAEQUIVALENT = "TRIP_VIAEQUIVALENT"
    TRIP_REALTIMEINCOMPLETE = "TRIP_REALTIMEINCOMPLETE"
    TRIP_ITTIMEEXTENDED = "TRIP_ITTIMEEXTENDED"
    TRIP_ITMODECHANGED = "TRIP_ITMODECHANGED"
    TRIP_INCONVENIENTWAITING = "TRIP_INCONVENIENTWAITING"
    TRIP_MULTIPOINT_NOTALLPOINTSCOVERED = "TRIP_MULTIPOINT_NOTALLPOINTSCOVERED"
    TRIP_MULTIPOINT_TOOMANYPOINTS = "TRIP_MULTIPOINT_TOOMANYPOINTS"
    TRIP_MULTIPOINT_TYPE_NOT_SUPPORTED = "TRIP_MULTIPOINT_TYPE_NOT_SUPPORTED"
    TRIP_REFINE_LEG_UNKNOWN = "TRIP_REFINE_LEG_UNKNOWN"
    REFINE_OBJECTNOTFOUND = "REFINE_OBJECTNOTFOUND"
    REFINE_PROFILENOTSUPPORTED = "REFINE_PROFILENOTSUPPORTED"
    TRIP_OTHER = "TRIP_OTHER"
