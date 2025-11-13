from enum import Enum

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


class CheckPointProcessEnumeration(Enum):
    """
    Allowed values for a CHECK CONSTRAINT.
    """

    NONE = "none"
    UNKNOWN = "unknown"
    TICKET_PURCHASE = "ticketPurchase"
    TICKET_COLLECTION = "ticketCollection"
    TICKET_VALIDATION = "ticketValidation"
    BAGGAGE_CHECK_IN = "baggageCheckIn"
    OVERSIZE_BAGGAGE_CHECK_IN = "oversizeBaggageCheckIn"
    OVERSIZE_BAGGAGE_RECLAIM = "oversizeBaggageReclaim"
    BAGGAGE_RECLAIM = "baggageReclaim"
    LEFT_LUGGAGE_DEPOSIT = "leftLuggageDeposit"
    LEFT_LUGGAGE_RECLAIM = "leftLuggageReclaim"
    FIRSTCLASS_CHECKIN = "firstclassCheckin"
    SPECIAL_NEEDS_CHECKIN = "specialNeedsCheckin"
    BAGGAGE_SECURITY_CHECK = "baggageSecurityCheck"
    SECURITY_CHECK = "securityCheck"
    OUTGOING_PASSPORT_CONTROL = "outgoingPassportControl"
    INCOMING_PASSPORT_CONTROL = "incomingPassportControl"
    FASTTRACK_DEPARTURES = "fasttrackDepartures"
    FASTTRACK_ARRIVALS = "fasttrackArrivals"
    INCOMING_DUTY_FREE = "incomingDutyFree"
    OUTGOING_DUTY_FREE = "outgoingDutyFree"
    TAX_REFUNDS = "taxRefunds"
    OUTGOING_CUSTOMS = "outgoingCustoms"
    INCOMING_CUSTOMS = "incomingCustoms"
