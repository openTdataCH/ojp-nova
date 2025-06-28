from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class AlternativeModesOfOperationEnumeration(Enum):
    """
    ALTERNATIVE MODE OF OPERATION offered.

    :cvar SHARING: Using a sharing as an ALTERNATIVE MODE OF OPERATION.
        Only if one of the specialisations doesn't apply.
    :cvar STATION_LESS_SHARING: ALTERNATIVE MODE OF OPERATION. station
        less sharing.
    :cvar STATION_BASED_SHARING: ALTERNATIVE MODE OF OPERATION. Based on
        fix stations (VEHICLE MEETING POINT).
    :cvar SINGLE_STATION_BASED_SHARING: ALTERNATIVE MODE OF OPERATION.
        Based on single fix station (VEHICLE MEETING POINT).
    :cvar MULTIPLE_STATION_BASED_SHARING: ALTERNATIVE MODE OF OPERATION.
        Based on multiple fix stations (VEHICLE MEETING POINT).
    :cvar PEER_TO_PEER_SHARING: ALTERNATIVE MODE OF OPERATION.
        Specialised sharing between people.
    :cvar PARK_AND_RIDE_SHARING: ALTERNATIVE MODE OF OPERATION.
        Specialised sharing in the context of a park and ride situation.
    :cvar SHARING_CLUB_SHARING: ALTERNATIVE MODE OF OPERATION. Sharing
        organised as a club.
    :cvar PR_M: ALTERNATIVE MODE OF OPERATION. In relation to a
        conventional SERVICE JOURNEY, but when pick-up and drop-off are
        not associated with SCHEDULED STOP POINTs.
    :cvar POOLING: General pooling ALTERNATIVE MODE OF OPERATION. Only
        use this enum when no specialisation applies. In some cases,
        where the pooling is very "scheduled" use the pooling in
        ConventionalModeOfOperation.
    :cvar TAXI: Taxi MODE OF OPERATION.
    :cvar SHUTTLE: Shuttle MODE OF OPERATION, when not associated with
        SCHEDULED STOP POINTs.
    :cvar DYNAMIC_POOLING: ALTERNATIVE MODE OF OPERATION. A pooling that
        is dynamic, usually local, and not long-term planned.
    :cvar LONG_DISTANCE_POOLING: ALTERNATIVE MODE OF OPERATION. A
        pooling for long distances, mostly for a SINGLE JOURNEY.
    :cvar COMMUTER_POOLING: ALTERNATIVE MODE OF OPERATION. A pooling to
        go to workplaces and related things. Usually, in a regular
        interval with the same people.
    :cvar PARK_AND_RIDE_POOLING: ALTERNATIVE MODE OF OPERATION. A
        pooling in relation to park and ride.
    :cvar CHAUFFEURED: ALTERNATIVE MODE OF OPERATION for SINGLE JOURNEY
        with a paid driver. Often more than a single SINGLE JOURNEY.
    :cvar DEMAND_RESPONSIVE: ALTERNATIVE MODE OF OPERATION demand
        responsive is used when there is no SCHEDULED STOP POINTs
        involved and the timetable component is weak. Otherwise, use the
        demandResponsive in ConventionalModeOfOperation.
    :cvar FLEXIBLE_AREA: Specialisation of the demand responsive
        ALTERNATIVE MODE OF OPERATION for AREA related offers.
        Otherwise, use the demandResponsive in
        ConventionalModeOfOperation.
    :cvar COMPANY_SHUTTLE: ALTERNATIVE MODE OF OPERATION. To
        specifically state that it is a company related. Specialisation
        of demand responsive.
    :cvar HOTEL_SHUTTLE: ALTERNATIVE MODE OF OPERATION. To specifically
        state that it is hotel related. Specialisation of demand
        responsive.
    :cvar HIRE: Using a hired VEHICLE.
    :cvar OTHER: Only use this value when no other applies.
    """

    SHARING = "sharing"
    STATION_LESS_SHARING = "stationLessSharing"
    STATION_BASED_SHARING = "stationBasedSharing"
    SINGLE_STATION_BASED_SHARING = "singleStationBasedSharing"
    MULTIPLE_STATION_BASED_SHARING = "multipleStationBasedSharing"
    PEER_TO_PEER_SHARING = "peerToPeerSharing"
    PARK_AND_RIDE_SHARING = "parkAndRideSharing"
    SHARING_CLUB_SHARING = "sharingClubSharing"
    PR_M = "prM"
    POOLING = "pooling"
    TAXI = "taxi"
    SHUTTLE = "shuttle"
    DYNAMIC_POOLING = "dynamicPooling"
    LONG_DISTANCE_POOLING = "longDistancePooling"
    COMMUTER_POOLING = "commuterPooling"
    PARK_AND_RIDE_POOLING = "parkAndRidePooling"
    CHAUFFEURED = "chauffeured"
    DEMAND_RESPONSIVE = "demandResponsive"
    FLEXIBLE_AREA = "flexibleArea"
    COMPANY_SHUTTLE = "companyShuttle"
    HOTEL_SHUTTLE = "hotelShuttle"
    HIRE = "hire"
    OTHER = "other"
