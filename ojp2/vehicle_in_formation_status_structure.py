from dataclasses import dataclass, field
from typing import Optional

from ojp2.accessibility_assessment_structure import (
    AccessibilityAssessmentStructure,
)
from ojp2.extensions_2 import Extensions2
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.vehicle_in_formation_status_enumeration import (
    VehicleInFormationStatusEnumeration,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VehicleInFormationStatusStructure:
    """
    Description of the status of a monitored vehicle.

    :ivar status: Status of vehicle.
    :ivar description: Description of the status of a formation or a
        vehicle within the formation.
    :ivar accessibility_assessment: Accessibility of the formation or a
        vehicle within the formation.
    :ivar extensions:
    """

    status: Optional[VehicleInFormationStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    description: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
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
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
