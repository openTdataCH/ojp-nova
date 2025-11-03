from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.modification_enumeration import ModificationEnumeration
from ojp2.status_enumeration import StatusEnumeration

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class VersionedObjectStructure:
    """
    Abstract Type for a versioned object.
    """

    created: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    last_updated: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastUpdated",
            "type": "Attribute",
            "required": True,
        },
    )
    modification: ModificationEnumeration = field(
        default=ModificationEnumeration.NEW,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    status: StatusEnumeration = field(
        default=StatusEnumeration.ACTIVE,
        metadata={
            "type": "Attribute",
        },
    )
