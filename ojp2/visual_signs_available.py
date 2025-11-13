from dataclasses import dataclass

from ojp2.accessibility_structure import AccessibilityStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class VisualSignsAvailable(AccessibilityStructure):
    """
    Whether a PLACE / SITE ELEMENT has Visual signals available for the visually
    impaired.
    """

    class Meta:
        namespace = "http://www.ifopt.org.uk/acsb"
