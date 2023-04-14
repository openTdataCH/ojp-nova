from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from ojp.booking_access_enumeration import BookingAccessEnumeration
from ojp.booking_method_list_of_enumerations import BookingMethodListOfEnumerations
from ojp.contact_details_structure import ContactDetailsStructure
from ojp.international_text_structure import InternationalTextStructure
from ojp.purchase_moment_list_of_enumerations import PurchaseMomentListOfEnumerations
from ojp.purchase_when_enumeration import PurchaseWhenEnumeration
from ojp.web_link_structure import WebLinkStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class BookingArrangementsStructure:
    """
    Type for BOOKING ARRANGEMENTs modified from NeTEx.

    :ivar booking_contact: Contact for Booking.
    :ivar booking_methods: Allowed Ways of Making a BOOKING.
    :ivar booking_access: Who can make a booking. Default is public.
    :ivar book_when: When Booking can be made.
    :ivar buy_when: When purchase can be made.
    :ivar latest_booking_time: Latest time that booking can be made. The
        exact meaning must be derived also from BookWhen and
        MinimumBookingPeriod.
    :ivar minimum_booking_period: Minimum interval in advance of
        departure day or time that Service may be ordered.
    :ivar maximum_booking_period: Maximum interval in advance of
        departure day or time that Service may be ordered.
    :ivar booking_url: URL for booking.
    :ivar booking_note: Note about booking the FLEXIBLE LINE.
    :ivar extension:
    """
    booking_contact: Optional[ContactDetailsStructure] = field(
        default=None,
        metadata={
            "name": "BookingContact",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    booking_methods: Optional[BookingMethodListOfEnumerations] = field(
        default=None,
        metadata={
            "name": "BookingMethods",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    booking_access: Optional[BookingAccessEnumeration] = field(
        default=None,
        metadata={
            "name": "BookingAccess",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    book_when: Optional[PurchaseWhenEnumeration] = field(
        default=None,
        metadata={
            "name": "BookWhen",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    buy_when: Optional[PurchaseMomentListOfEnumerations] = field(
        default=None,
        metadata={
            "name": "BuyWhen",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    latest_booking_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LatestBookingTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    minimum_booking_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumBookingPeriod",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    maximum_booking_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumBookingPeriod",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    booking_url: Optional[WebLinkStructure] = field(
        default=None,
        metadata={
            "name": "BookingUrl",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    booking_note: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "BookingNote",
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
