from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class OccupancyEnumeration(Enum):
    """Passenger load status of a VEHICLE - GTFS-R / TPEG Pts045

    :cvar UNKNOWN: TPEG Pts45_0, unknown
    :cvar EMPTY: GTFS-R "EMPTY" The vehicle is considered empty by most
        measures, and has few or no passengers onboard, but is still
        accepting passengers.
    :cvar MANY_SEATS_AVAILABLE: GTFS-R "MANY_SEATS_AVAILABLE" / TPEG
        Pts45_1, many seats available The vehicle has a large percentage
        of seats available. What percentage of free seats out of the
        total seats available is to be considered large enough to fall
        into this category is determined at the discretion of the
        producer.
    :cvar FEW_SEATS_AVAILABLE: GTFS-R "FEW_SEATS_AVAILABLE" / TPEG
        Pts45_2, few seats available The vehicle has a small percentage
        of seats available. What percentage of free seats out of the
        total seats available is to be considered small enough to fall
        into this category is determined at the discretion of the
        producer.
    :cvar STANDING_ROOM_ONLY: GTFS-R "STANDING_ROOM_ONLY" / TPEG
        Pts45_4, standing room only (and TPEG Pts45_3, no seats
        available) The vehicle can currently accommodate only standing
        passengers.
    :cvar CRUSHED_STANDING_ROOM_ONLY: GTFS-R
        "CRUSHED_STANDING_ROOM_ONLY" The vehicle can currently
        accommodate only standing passengers and has limited space for
        them.
    :cvar FULL: GTFS-R "FULL" / TPEG Pts45_5, full
    :cvar NOT_ACCEPTING_PASSENGERS: GTFS-R "NOT_ACCEPTING_PASSENGERS"
        The vehicle cannot accept passengers.
    :cvar UNDEFINED: TPEG Pts45_255, undefined occupancy
    :cvar SEATS_AVAILABLE: (SIRI 2.1) deprecated - use a more specific
        value
    :cvar STANDING_AVAILABLE: (SIRI 2.1) deprecated - use a more
        specific value
    """

    UNKNOWN = "unknown"
    EMPTY = "empty"
    MANY_SEATS_AVAILABLE = "manySeatsAvailable"
    FEW_SEATS_AVAILABLE = "fewSeatsAvailable"
    STANDING_ROOM_ONLY = "standingRoomOnly"
    CRUSHED_STANDING_ROOM_ONLY = "crushedStandingRoomOnly"
    FULL = "full"
    NOT_ACCEPTING_PASSENGERS = "notAcceptingPassengers"
    UNDEFINED = "undefined"
    SEATS_AVAILABLE = "seatsAvailable"
    STANDING_AVAILABLE = "standingAvailable"
