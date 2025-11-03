from dataclasses import dataclass

from ojp2.accessibility_structure import AccessibilityStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class WheelchairAccess(AccessibilityStructure):
    """Whether a PLACE / SITE ELEMENT is wheelchair accessible.

    Default is 'false'.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"
