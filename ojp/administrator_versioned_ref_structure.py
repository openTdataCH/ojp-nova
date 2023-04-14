from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ojp.modification_enumeration import ModificationEnumeration
from ojp.status_enumeration import StatusEnumeration

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AdministratorVersionedRefStructure:
    """
    Type for a versioned reference to an ORGANISATION with administrative
    responsibility.
    """
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    last_updated: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastUpdated",
            "type": "Attribute",
        }
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "type": "Attribute",
        }
    )
