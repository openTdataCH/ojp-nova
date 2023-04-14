from enum import Enum

__NAMESPACE__ = "http://www.vdv.de/ojp"


class ReservationNeededEnumeration(Enum):
    """
    Possible types of reservation needed for services.

    :cvar NONE:
    :cvar SERVICE: A reservation/booking is required for the service to
        operate. BookingArrangement should then be used and contain more
        details.
    :cvar STOP: A reservation/booking is required for the service to
        call at the stop for boarding and alighting. BookingArrangement
        should then be used and contain more details.
    """
    NONE = "none"
    SERVICE = "service"
    STOP = "stop"
