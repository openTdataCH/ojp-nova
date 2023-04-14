from dataclasses import dataclass, field
from typing import List, Optional
from ojp.accessibility_assessment_structure import AccessibilityAssessmentStructure
from ojp.extensions_1 import Extensions1
from ojp.facility_status_enumeration import FacilityStatusEnumeration
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FacilityStatusStructure:
    """
    Descriprion of the status of a MONITORED FACILITY.

    :ivar status: Status of the facility.
    :ivar description: Description of the facility Status.  (Unbounded
        since SIRI 2.0)
    :ivar accessibility_assessment: Accessibility of the facility.
    :ivar extensions:
    """
    status: Optional[FacilityStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    description: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
