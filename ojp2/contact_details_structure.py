from dataclasses import dataclass, field
from typing import Optional

from ojp2.international_text_structure import InternationalTextStructure
from ojp2.web_link_structure import WebLinkStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ContactDetailsStructure:
    """
    Type for contact details.

    :ivar contact_person: Name of contact person.
    :ivar email: The email address of the contact.
    :ivar phone: Contact telephone number.
    :ivar fax: Contact fax number.
    :ivar url: The website address of the contact.
    :ivar further_details: Further details about contact process.
    """

    contact_person: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "ContactPerson",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    url: Optional[WebLinkStructure] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    further_details: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "FurtherDetails",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
