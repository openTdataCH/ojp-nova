from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class TicketingFacilityEnumeration(Enum):
    """
    Values for Ticketing Facility.
    """

    UNKNOWN = "unknown"
    TICKET_MACHINES = "ticketMachines"
    TICKET_OFFICE = "ticketOffice"
    TICKET_ON_DEMAND_MACHINES = "ticketOnDemandMachines"
    TICKET_SALES = "ticketSales"
    MOBILE_TICKETING = "mobileTicketing"
    TICKET_COLLECTION = "ticketCollection"
    CENTRAL_RESERVATIONS = "centralReservations"
    LOCAL_TICKETS = "localTickets"
    NATIONAL_TICKETS = "nationalTickets"
    INTERNATIONAL_TICKETS = "internationalTickets"
