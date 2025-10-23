from dataclasses import dataclass, field
from typing import List, Optional
from ojp.accessibility_limitation_structure import AccessibilityLimitationStructure
from ojp.extensions_2 import Extensions2
from ojp.suitability_structure import SuitabilityStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class AccessibilityAssessmentStructure:
    """
    Type for Assesment.

    :ivar mobility_impaired_access: Summary indication as to whether the
        component is considered to be accessible or not.
    :ivar limitations: The Limitations that apply to component.
    :ivar suitabilities: The Suitability of the component to meet
        specifc user needs.
    :ivar extensions:
    """
    mobility_impaired_access: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MobilityImpairedAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
            "required": True,
        }
    )
    limitations: Optional["AccessibilityAssessmentStructure.Limitations"] = field(
        default=None,
        metadata={
            "name": "Limitations",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        }
    )
    suitabilities: Optional["AccessibilityAssessmentStructure.Suitabilities"] = field(
        default=None,
        metadata={
            "name": "Suitabilities",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        }
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )

    @dataclass
    class Limitations:
        """
        :ivar accessibility_limitation: The accessibility limitations of
            a component.
        """
        accessibility_limitation: List[AccessibilityLimitationStructure] = field(
            default_factory=list,
            metadata={
                "name": "AccessibilityLimitation",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Suitabilities:
        """
        :ivar suitability: The Suitability of com[onent to meet a
            specifc user need.
        """
        suitability: List[SuitabilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
                "min_occurs": 1,
            }
        )
