from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TicketRestrictionEnumeration(Enum):
    """
    Values for TicketRestrictionTypeTPEG pti_table 25.
    """
    PTI25_0 = "pti25_0"
    UNKNOWN = "unknown"
    PTI25_1 = "pti25_1"
    ALL_TICKET_CLASSES_VALID = "allTicketClassesValid"
    PTI25_2 = "pti25_2"
    FULL_FARE_ONLY = "fullFareOnly"
    PTI25_3 = "pti25_3"
    CERTAIN_TICKETS_ONLY = "certainTicketsOnly"
    PTI25_4 = "pti25_4"
    TICKET_WITH_RESERVATION = "ticketWithReservation"
    PTI25_5 = "pti25_5"
    SPECIAL_FARE = "specialFare"
    PTI25_6 = "pti25_6"
    ONLY_TICKETS_OF_SPECIFIED_OPERATOR = "onlyTicketsOfSpecifiedOperator"
    PTI25_7 = "pti25_7"
    NO_RESTRICTIONS = "noRestrictions"
    PTI25_8 = "pti25_8"
    NO_OFF_PEAK_TICKETS = "noOffPeakTickets"
    PTI25_9 = "pti25_9"
    NO_WEEKEND_RETURN_TICKETS = "noWeekendReturnTickets"
    PTI25_10 = "pti25_10"
    NO_REDUCED_FARE_TICKETS = "noReducedFareTickets"
    PTI25_255 = "pti25_255"
    UNKNOWN_TICKET_RESTRICTION = "unknownTicketRestriction"
