from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SimpleContactStructure:
    """
    Type for Simple Contact Details.

    :ivar phone_number: Phone number +SIRI v2.0
    :ivar url: Url for contact +SIRI v2.0
    """
    phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
