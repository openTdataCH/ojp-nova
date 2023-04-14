from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class HierarchyEnumeration(Enum):
    """Indicates for which parts of the hierarchy of the StopPlace(s) stop
    events should be provided (if known by the server).

    "local" (default) is the local server setting. "no" will include no
    hierarchy and only provide the given StopPlace / StopPoint. "down"
    will include all lower StopPoints/StopPlaces in the hierarchy, if
    such a hierarchy exists. "all" does include all
    StopPoints/StopPlaces for the meta station, if it is known. How to
    use this: if you indicate the reference to a train station and the
    parameter is set to "down", the departures/ arrivals at the
    associated bus stations will show as well. If you have the
    ScheduledStopPoint of platform B of the local bus and it is
    associated with 3 other stations, you will get all these
    arrivals/departures as well, if the parameter is set to "all".
    """
    LOCAL = "local"
    NO = "no"
    DOWN = "down"
    ALL = "all"
