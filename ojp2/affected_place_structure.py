from dataclasses import dataclass, field
from typing import Optional

from ojp2.accessibility_assessment_structure import (
    AccessibilityAssessmentStructure,
)
from ojp2.extensions_2 import Extensions2
from ojp2.location_structure import LocationStructure
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedPlaceStructure:
    """
    Type for annotated references to a TOPOGRAPHIC PLACE.

    :ivar place_ref: Reference to a SITE or TOPOGRAPHIC PLACE
        (Locality).
    :ivar private_code: Alternative identifier of SITE or TOPOGRAPHIC
        PLACE
    :ivar place_name: Name of SITE or TOPOGRAPHIC PLACE (locality) in
        which stop is found.  (Unbounded since SIRI 2.0)
    :ivar location: Spatial coordinates of STOP POINT. Derivable from
        StopRef.
    :ivar place_category: Category of TOPOGRAPHIC PLACE or SITE.
    :ivar equipment_ref: Reference to an EQUIPMENT found at SITE.
    :ivar accessibility_assessment: Changes to accessibility for SITE.
    :ivar extensions:
    """

    place_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    private_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "PlaceName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    place_category: Optional[str] = field(
        default=None,
        metadata={
            "name": "PlaceCategory",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    equipment_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentRef",
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
