from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class VehicleProgressEnumeration(Enum):
    """
    Vehicle progress relative to timetable service pattern.
    """

    NOT_YET_OPERATED = "Not yet operated"
    OPERATION_FINISHED = "Operation finished"
    AT_STOP = "At stop"
    BETWEEN_STOPS = "Between stops"
