from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from ojp.international_text_structure import InternationalTextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class BookingArrangementStructure:
    """
    [a more generalised form of BOOKING ARRANGEMENTS in TMv6] arrangement for
    booking any leg or legs of a journey.

    :ivar booking_agency_name: Name of the booking agency (contractual
        partner).
    :ivar booking_url: URL to online booking service.
    :ivar info_url: URL to information page.
    :ivar phone_number: Phone number for booking.
    :ivar minimum_booking_period: Minimum duration bookings must be
        completed before trip starts.
    :ivar extension:
    """
    booking_agency_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "BookingAgencyName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    booking_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingUrl",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    info_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfoUrl",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    minimum_booking_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumBookingPeriod.",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
