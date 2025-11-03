from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TicketRestrictionEnumeration(Enum):
    """Values for TPEG Pti025 - TicketRestrictionType

    :cvar UNKNOWN: TPEG Pti25_0, unknown
    :cvar ALL_TICKET_CLASSES_VALID: TPEG Pti25_1, all ticket classes
        valid
    :cvar FULL_FARE_ONLY: TPEG Pti25_2, full fare only
    :cvar CERTAIN_TICKETS_ONLY: TPEG Pti25_3, certain tickets only
    :cvar TICKET_WITH_RESERVATION: TPEG Pti25_4, ticket with reservation
    :cvar SPECIAL_FARE: TPEG Pti25_5, special fare
    :cvar ONLY_TICKETS_OF_SPECIFIED_OPERATOR: TPEG Pti25_6, only tickets
        of specified operator
    :cvar NO_RESTRICTIONS: TPEG Pti25_7, no restrictions
    :cvar NO_OFF_PEAK_TICKETS: TPEG Pti25_8, no off-peak tickets
    :cvar NO_WEEKEND_RETURN_TICKETS: TPEG Pti25_9, no weekend return
        tickets
    :cvar NO_REDUCED_FARE_TICKETS: TPEG Pti25_10, no reduced fare
        tickets
    :cvar UNKNOWN_TICKET_RESTRICTION: TPEG Pti25_255, unknown ticket
        restriction
    """

    UNKNOWN = "unknown"
    ALL_TICKET_CLASSES_VALID = "allTicketClassesValid"
    FULL_FARE_ONLY = "fullFareOnly"
    CERTAIN_TICKETS_ONLY = "certainTicketsOnly"
    TICKET_WITH_RESERVATION = "ticketWithReservation"
    SPECIAL_FARE = "specialFare"
    ONLY_TICKETS_OF_SPECIFIED_OPERATOR = "onlyTicketsOfSpecifiedOperator"
    NO_RESTRICTIONS = "noRestrictions"
    NO_OFF_PEAK_TICKETS = "noOffPeakTickets"
    NO_WEEKEND_RETURN_TICKETS = "noWeekendReturnTickets"
    NO_REDUCED_FARE_TICKETS = "noReducedFareTickets"
    UNKNOWN_TICKET_RESTRICTION = "unknownTicketRestriction"
