from dataclasses import dataclass, field
from ojp.accessibility_enumeration import AccessibilityEnumeration

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class StepFreeAccess:
    """
    Whether a PLACE / SITE ELEMENT has step free access.
    """
    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"

    value: AccessibilityEnumeration = field(
        default=AccessibilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
