from dataclasses import dataclass, field
from typing import Optional

from ojp2.accessibility_assessment_structure import (
    AccessibilityAssessmentStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedStopPlaceElementStructure:
    """
    Type for information about the quays affected by an SITUATION.

    :ivar accessibility_assessment: Disruption of accessibility.
    """

    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = (
        field(
            default=None,
            metadata={
                "name": "AccessibilityAssessment",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
