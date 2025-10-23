from dataclasses import dataclass, field
from ojp.booking_status_enumeration import BookingStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class BookingStatusType:
    """Booking Status - Tpeg Report Type pti24."""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: BookingStatusEnumeration = field(
        default=BookingStatusEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
