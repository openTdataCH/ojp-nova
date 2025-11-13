from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class RoutePointTypeEnumeration(Enum):
    """Values for ROUTE POINT type that correspond to TPEG Pts44: StopPlaceUsage (Pti15: deprecated since SIRI 2.1).

    :cvar UNKNOWN: TPEG Pti15_0, Pts44_0, unknown
    :cvar ORIGIN: TPEG Pts44_1, origin
    :cvar DESTINATION: TPEG Pti15_2, Pts44_2, destination
    :cvar INTERMEDIATE: TPEG Pts44_3, intermediate.
    :cvar LEG_BOARD: TPEG Pts44_4, leg board
    :cvar LEG_INTERMEDIATE: TPEG Pts44_5, leg intermediate
    :cvar LEG_ALIGHT: TPEG Pts44_6, leg alight
    :cvar FIRST_ROUTE_POINT: TPEG Pts44_7, first route point
    :cvar LAST_ROUTE_POINT: TPEG Pts44_8, last route point
    :cvar AFFECTED_STOPPLACE: TPEG Pts44_9, affected STOP PLACE
    :cvar PRESENTED_STOPPLACE: TPEG Pts44_10, presented STOP PLACE
    :cvar UNDEFINED_STOPPLACE_USAGE: TPEG Pts44_255, undefined STOP
        PLACE usage
    :cvar START_POINT: DEPRECATED since SIRI 2.1 and replaced by Pts44_1
        value 'origin' (TPEG Pti15_1 - start point) .
    :cvar STOP: DEPRECATED since SIRI 2.1 (TPEG Pti15_3 - stop)
    :cvar VIA: DEPRECATED since SIRI 2.1 (TPEG Pti15_4 - via)
    :cvar NOT_STOPPING: DEPRECATED since SIRI 2.1 (TPEG Pti15_5 - not-
        stopping)
    :cvar TEMPORARY_STOP: DEPRECATED since SIRI 2.1 (TPEG Pti15_6 -
        temporary stop)
    :cvar TEMPORARILY_NOT_STOPPING: DEPRECATED since SIRI 2.1 (TPEG
        Pti15_7 - temporarily not-stopping)
    :cvar EXCEPTIONAL_STOP: DEPRECATED since SIRI 2.1 (TPEG Pti15_8 -
        exceptional stop)
    :cvar ADDITIONAL_STOP: DEPRECATED since SIRI 2.1 (TPEG Pti15_9 -
        additional stop)
    :cvar REQUEST_STOP: DEPRECATED since SIRI 2.1 (TPEG Pti15_10 -
        request stop)
    :cvar FRONT_TRAIN_DESTINATION: DEPRECATED since SIRI 2.1 (TPEG
        Pti15_11 - front train destination)
    :cvar REAR_TRAIN_DESTINATION: DEPRECATED since SIRI 2.1 (TPEG
        Pti15_12 - rear train destination)
    :cvar THROUGH_SERVICE_DESTINATION: DEPRECATED since SIRI 2.1 (TPEG
        Pti15_13 - through service destination)
    :cvar NOT_VIA: DEPRECATED since SIRI 2.1 (TPEG Pti15_14 - not via)
    :cvar ALTERED_START_POINT: DEPRECATED since SIRI 2.1 (TPEG Pti15_15
        - altered start point)
    :cvar ALTERED_DESTINATION: DEPRECATED since SIRI 2.1 (TPEG Pti15_16
        - altered destination)
    :cvar UNDEFINED_ROUTE_POINT: DEPRECATED since SIRI 2.1 (TPEG
        Pti15_255 - undefined route point)
    """

    UNKNOWN = "unknown"
    ORIGIN = "origin"
    DESTINATION = "destination"
    INTERMEDIATE = "intermediate"
    LEG_BOARD = "legBoard"
    LEG_INTERMEDIATE = "legIntermediate"
    LEG_ALIGHT = "legAlight"
    FIRST_ROUTE_POINT = "firstRoutePoint"
    LAST_ROUTE_POINT = "lastRoutePoint"
    AFFECTED_STOPPLACE = "affectedStopplace"
    PRESENTED_STOPPLACE = "presentedStopplace"
    UNDEFINED_STOPPLACE_USAGE = "undefinedStopplaceUsage"
    START_POINT = "startPoint"
    STOP = "stop"
    VIA = "via"
    NOT_STOPPING = "notStopping"
    TEMPORARY_STOP = "temporaryStop"
    TEMPORARILY_NOT_STOPPING = "temporarilyNotStopping"
    EXCEPTIONAL_STOP = "exceptionalStop"
    ADDITIONAL_STOP = "additionalStop"
    REQUEST_STOP = "requestStop"
    FRONT_TRAIN_DESTINATION = "frontTrainDestination"
    REAR_TRAIN_DESTINATION = "rearTrainDestination"
    THROUGH_SERVICE_DESTINATION = "throughServiceDestination"
    NOT_VIA = "notVia"
    ALTERED_START_POINT = "alteredStartPoint"
    ALTERED_DESTINATION = "alteredDestination"
    UNDEFINED_ROUTE_POINT = "undefinedRoutePoint"
