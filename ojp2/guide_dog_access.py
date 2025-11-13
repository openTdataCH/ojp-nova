from dataclasses import dataclass

from ojp2.accessibility_structure import AccessibilityStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class GuideDogAccess(AccessibilityStructure):
    """
    Whether a PLACE / SITE ELEMENT allows guide dog access.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"
