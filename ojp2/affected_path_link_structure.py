from dataclasses import dataclass, field
from typing import Optional

from ojp2.accessibility_feature_enumeration_2 import (
    AccessibilityFeatureEnumeration2,
)
from ojp2.extensions_2 import Extensions2
from ojp2.link_projection_structure import LinkProjectionStructure
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.offset_structure import OffsetStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedPathLinkStructure:
    """
    Information about a CONNECTION link from a given stop affected by a SITUATION.

    :ivar link_ref: Identifier of CONNECTION link.
    :ivar link_name: Description of Link.  (Unbounded since SIRI 2.0)
    :ivar accessibility_feature: Nature of CONNECTION link.
    :ivar link_direction: Description of a DIRECTION of CONNECTION link.
    :ivar link_projection: GIs projection of Section. NB Line here means
        Geometry Polyline, not Transmodel Transport Line.
    :ivar offset: Offset from start or end of section to use when
        projecting.
    :ivar extensions:
    """

    link_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "LinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "LinkName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_feature: Optional[AccessibilityFeatureEnumeration2] = field(
        default=None,
        metadata={
            "name": "AccessibilityFeature",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_direction: list[str] = field(
        default_factory=list,
        metadata={
            "name": "LinkDirection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_projection: Optional[LinkProjectionStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
