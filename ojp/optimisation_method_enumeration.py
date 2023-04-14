from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class OptimisationMethodEnumeration(Enum):
    """
    the types of algorithm that can be used for planning a journey (fastest,
    least walking, etc).
    """
    FASTEST = "fastest"
    MIN_CHANGES = "minChanges"
    LEAST_WALKING = "leastWalking"
    LEAST_COST = "leastCost"
    EARLIEST_ARRIVAL = "earliestArrival"
    LATEST_DEPARTURE = "latestDeparture"
    EARLIEST_ARRIVAL_AND_LATEST_DEPARTURE = "earliestArrivalAndLatestDeparture"
