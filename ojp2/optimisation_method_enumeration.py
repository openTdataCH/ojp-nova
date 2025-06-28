from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class OptimisationMethodEnumeration(Enum):
    """The types of algorithms that can be used for planning a journey (fastest,
    least walking, etc.).

    Only one method can be used. Each one really is a whole set of a
    policy, which is defined below. E.g., "fastest" also includes "least
    transfers" as a second criteria, some modes are excluded usually by
    default. Implementations might differ (slightly). Also, some
    strategies might not be implemented. The most important strategies
    are marked.

    :cvar FASTEST: Shortest duration somewhere in the future. This may
        present a shorter trip than the next earliest arrival (with
        latest departure). Expected strategy.
    :cvar MIN_CHANGES: Minimise the number of interchanges as the first
        criterion. Expected strategy.
    :cvar LEAST_WALKING: Shortest walking distance in meters, summed
        over all legs.
    :cvar LEAST_COST: Cheapest fare, considering the applicable
        reductions. Might not be based on actual cost, but an
        estimation. Expected strategy.
    :cvar LEAST_DISTANCE: Least distance in metres. Mostly used for
        ALTERNATIVE MODE OF OPERATION and for ItModesToCover.
    :cvar EARLIEST_ARRIVAL: Earliest possible arrival time respecting
        the time constraints (forward search).
    :cvar LATEST_DEPARTURE: Latest departure time for a given arrival
        time (backward search).
    :cvar EARLIEST_ARRIVAL_AND_LATEST_DEPARTURE: Combines
        earliestArrival and latestDeparture, allowing to compress the
        departure time (forward-backward-forward search).
    :cvar MIN_NON_LEVEL_ENTRANCES: The user wants to minimize non-level
        entrances on the trip. this is useful for PRM who still can use
        some non-level entrances.
    :cvar MIN_STAIRS: The user wants to minimize stairs and steps on the
        trip. This is useful for PRM who still can use some
        steps/stairs.
    :cvar BEST_FOR_VISUAL_IMPAIRMENT: The user wants to avoid transfers
        without tactile guidance, as well as platforms and vehicles
        without auditory signals.
    :cvar BEST_FOR_AUDITORY_IMPAIRMENT: The user wants to avoid
        transfers without guidance for people with auditory impairment,
        as well as platforms and vehicles without visual signs.
    :cvar ENVIRONMENTAL_SAFETY: If set, favour "green" modes/lines such
        as bike sharing and (electric) trains, avoid or restrict
        modes/lines known for higher CO2 emissions such as
        (conventional) taxi, ride-hailing or coach.
    :cvar EXTRA_SAFE: High level of safety (referring to crime, hazards
        or prone to accidents). If used, certain modes, lines or
        zones/districts known for lower safety, i.e. higher risk of
        accidents and crime, may be avoided, others may be preferred.
        This may depend on the actual, local or time of day situation.
        E.g. bike or scooter may be considered unsafe in some
        cities/districts while safe in others.
    :cvar EXTRA_RELIABLE: Low probability of delays, cancellations etc.
        If used, modes known for their (un)reliability may be
        avoided/preferred, and extra time added for transfers. This may
        depend on the actual, local or time of day situation, based on
        punctuality statics, traffic jam statistics or rush hours. E.g.
        taxis in a given city might be known to be unreliable during at
        8-10 and 16-19 hours, otherwise reliable.
    :cvar SCENIC: Scenic (or touristic) travel. Different by modes or by
        the surrounding.
    :cvar QUIET_TRAVEL: E.g. first class or quiet compartments
        preferred. Journeys that are with low occupancy.
    """

    FASTEST = "fastest"
    MIN_CHANGES = "minChanges"
    LEAST_WALKING = "leastWalking"
    LEAST_COST = "leastCost"
    LEAST_DISTANCE = "leastDistance"
    EARLIEST_ARRIVAL = "earliestArrival"
    LATEST_DEPARTURE = "latestDeparture"
    EARLIEST_ARRIVAL_AND_LATEST_DEPARTURE = "earliestArrivalAndLatestDeparture"
    MIN_NON_LEVEL_ENTRANCES = "minNonLevelEntrances"
    MIN_STAIRS = "minStairs"
    BEST_FOR_VISUAL_IMPAIRMENT = "bestForVisualImpairment"
    BEST_FOR_AUDITORY_IMPAIRMENT = "bestForAuditoryImpairment"
    ENVIRONMENTAL_SAFETY = "environmentalSafety"
    EXTRA_SAFE = "extraSafe"
    EXTRA_RELIABLE = "extraReliable"
    SCENIC = "scenic"
    QUIET_TRAVEL = "quietTravel"
