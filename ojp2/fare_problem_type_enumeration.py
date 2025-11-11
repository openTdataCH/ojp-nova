from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class FareProblemTypeEnumeration(Enum):
    """
    Types of problems that may be returned in responses to FARE requests.

    :cvar FARE_OUTOFAREA: The trip planning has found a route that
        leaves the area of the fare authority.
    :cvar FARE_JOURNEYNOTPERMITTED: The trip planning result suggests a
        service which is not permitted by the fare authority.
    :cvar FARE_ADDITIONALCHARGES: Passengers may be charged additional
        fees (e.g.: for road tolls or seat reservation).
    :cvar FARE_ADDITIONALTICKETS: Additional tickets may be necessary
        because only parts of the passenger trip could be covered.
    :cvar FARE_ROUTENOTFEASIBLE: Fare calculation is not possible
        because the suggested trip is not in compliance with the fare
        regulations, e.g., because of round trips, LEGs that go forth
        and return or exceed the maximal total trip duration.
    :cvar FARE_ALREADYCOVERED: The ticket that has been specified in the
        request is valid for the suggested trip (or parts of it as
        defined by LegRange).
    :cvar FARE_DATEOUTOFRANGE: The fare request cannot be processed
        because there is no information available for the requested
        date.
    :cvar FARE_STOPPOINTUNKNOWN: The fare request cannot be processed
        because the requested stop is unknown.
    :cvar FARE_OTHER: A problem has occurred that does not have a
        specific problem type.
    """

    FARE_OUTOFAREA = "FARE_OUTOFAREA"
    FARE_JOURNEYNOTPERMITTED = "FARE_JOURNEYNOTPERMITTED"
    FARE_ADDITIONALCHARGES = "FARE_ADDITIONALCHARGES"
    FARE_ADDITIONALTICKETS = "FARE_ADDITIONALTICKETS"
    FARE_ROUTENOTFEASIBLE = "FARE_ROUTENOTFEASIBLE"
    FARE_ALREADYCOVERED = "FARE_ALREADYCOVERED"
    FARE_DATEOUTOFRANGE = "FARE_DATEOUTOFRANGE"
    FARE_STOPPOINTUNKNOWN = "FARE_STOPPOINTUNKNOWN"
    FARE_OTHER = "FARE_OTHER"
