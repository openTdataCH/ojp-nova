from dataclasses import dataclass, field
from typing import Optional

from ojp2.accessibility_enumeration import AccessibilityEnumeration

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class AccessibilityStructure:
    """
    Type for accessibility.
    """

    value: Optional[AccessibilityEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
