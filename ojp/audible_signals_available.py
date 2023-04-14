from dataclasses import dataclass, field
from ojp.accessibility_enumeration import AccessibilityEnumeration

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class AudibleSignalsAvailable:
    """
    Whether a PLACE / SITE ELEMENT is wheelchair accessible.
    """
    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"

    value: AccessibilityEnumeration = field(
        default=AccessibilityEnumeration.FALSE,
        metadata={
            "required": True,
        }
    )
