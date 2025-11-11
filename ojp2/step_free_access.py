from dataclasses import dataclass

from ojp2.accessibility_structure import AccessibilityStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class StepFreeAccess(AccessibilityStructure):
    """Whether a PLACE / SITE ELEMENT has step free access.

    Default is 'unknown'.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"
