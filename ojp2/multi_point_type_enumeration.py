from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class MultiPointTypeEnumeration(Enum):
    """Defines how the router should handle requests with multiple origins and
    destinations.

    MultiPointType is more important than NumberOfResults in the sense
    that if 10 results are needed to fulfill the MultiPointType, then it
    is 10, even when NumberOfResults was set to 1.

    :cvar ANY_POINT: Returning results for a single origin and
        destination (hopefully the best ones). As this element was not
        sufficiently defined in the past, some implementations may
        behave differently.
    :cvar EACH_ORIGIN: At least a distinct solution for each of the
        origin points must be delivered.
    :cvar EACH_DESTINATION: At least a distinct solution for each of the
        destination points must be delivered.
    :cvar EACH_ORIGIN_DESTINATION: At least one result for each
        origin/destination pair must be delivered.
    :cvar SOME_POINTS: Clarifies that some (probably the "best") origin-
        destination pairs should be returned. How many are to be used is
        not defined.
    """

    ANY_POINT = "anyPoint"
    EACH_ORIGIN = "eachOrigin"
    EACH_DESTINATION = "eachDestination"
    EACH_ORIGIN_DESTINATION = "eachOriginDestination"
    SOME_POINTS = "somePoints"
