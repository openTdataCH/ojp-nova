from dataclasses import dataclass, field
from typing import Optional

from ojp2.accessibility_assessment_structure import (
    AccessibilityAssessmentStructure,
)
from ojp2.all_facilities_feature_structure import AllFacilitiesFeatureStructure
from ojp2.audible_signals_available import AudibleSignalsAvailable
from ojp2.escalator_free_access import EscalatorFreeAccess
from ojp2.extensions_2 import Extensions2
from ojp2.facility_category_enumeration import FacilityCategoryEnumeration
from ojp2.facility_location_structure import FacilityLocationStructure
from ojp2.lift_free_access import LiftFreeAccess
from ojp2.monitoring_validity_condition_structure import (
    MonitoringValidityConditionStructure,
)
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.organisation_ref_structure import OrganisationRefStructure
from ojp2.step_free_access import StepFreeAccess
from ojp2.suitability_structure import SuitabilityStructure
from ojp2.visual_signs_available import VisualSignsAvailable
from ojp2.wheelchair_access import WheelchairAccess

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FacilityStructure:
    """
    Type for description of the MONITORED FACILITY itself.

    :ivar facility_code: Identfier of Facility.
    :ivar description: Textual description of the facility.  (Unbounded
        since SIRI 2.0)
    :ivar facility_class: Type of facility (several types may be
        associated to a single facility)
    :ivar features: Features of service.
    :ivar owner_ref: Refererence to identifier of owner of facility.
    :ivar owner_name: Textual description of the owner of the facility.
    :ivar validity_condition: When Facility is normally avaialble. If
        not specified, default is 'always'. Values are Logically ANDed
        together.
    :ivar facility_location: Describes where the facility is located.
        The location is a Transmodel object reference or an NeTEx object
        reference.
    :ivar limitations: Limitation of facility.
    :ivar suitabilities: Suitabilities of facility for specific
        passenger needs.
    :ivar accessibility_assessment: Accessibility of the facility.
    :ivar extensions:
    """

    facility_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
    facility_class: list[FacilityCategoryEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FacilityClass",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    features: Optional["FacilityStructure.Features"] = field(
        default=None,
        metadata={
            "name": "Features",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    owner_ref: Optional[OrganisationRefStructure] = field(
        default=None,
        metadata={
            "name": "OwnerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    owner_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "OwnerName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_condition: Optional[MonitoringValidityConditionStructure] = field(
        default=None,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_location: Optional[FacilityLocationStructure] = field(
        default=None,
        metadata={
            "name": "FacilityLocation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    limitations: Optional["FacilityStructure.Limitations"] = field(
        default=None,
        metadata={
            "name": "Limitations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    suitabilities: Optional["FacilityStructure.Suitabilities"] = field(
        default=None,
        metadata={
            "name": "Suitabilities",
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

    @dataclass
    class Features:
        """
        :ivar feature: Description of the feauture of the facility.
            Several features may be associated to a single facility.
        """

        feature: list[AllFacilitiesFeatureStructure] = field(
            default_factory=list,
            metadata={
                "name": "Feature",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Limitations:
        """
        :ivar wheelchair_access:
        :ivar step_free_access:
        :ivar escalator_free_access:
        :ivar lift_free_access:
        :ivar audible_signals_available: Whether a PLACE / SITE ELEMENT
            has Audible signals for the visually impaired. Default is
            'false'.
        :ivar visual_signs_available: Whether a PLACE / SITE ELEMENT has
            Visual signals for the hearing impaired. Default is
            'unknown'.
        """

        wheelchair_access: Optional[WheelchairAccess] = field(
            default=None,
            metadata={
                "name": "WheelchairAccess",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
                "required": True,
            },
        )
        step_free_access: Optional[StepFreeAccess] = field(
            default=None,
            metadata={
                "name": "StepFreeAccess",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )
        escalator_free_access: Optional[EscalatorFreeAccess] = field(
            default=None,
            metadata={
                "name": "EscalatorFreeAccess",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )
        lift_free_access: Optional[LiftFreeAccess] = field(
            default=None,
            metadata={
                "name": "LiftFreeAccess",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )
        audible_signals_available: Optional[AudibleSignalsAvailable] = field(
            default=None,
            metadata={
                "name": "AudibleSignalsAvailable",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )
        visual_signs_available: Optional[VisualSignsAvailable] = field(
            default=None,
            metadata={
                "name": "VisualSignsAvailable",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )

    @dataclass
    class Suitabilities:
        """
        :ivar suitability: Type of specific need for wich the facility
            is appropriate.
        """

        suitability: list[SuitabilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
