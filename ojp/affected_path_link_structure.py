from dataclasses import dataclass, field
from typing import List, Optional
from ojp.accessibility_feature_enumeration import AccessibilityFeatureEnumeration
from ojp.extensions_1 import Extensions1
from ojp.link_projection_structure import LinkProjectionStructure
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.offset_structure import OffsetStructure

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
    link_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    link_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "LinkName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    accessibility_feature: Optional[AccessibilityFeatureEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessibilityFeature",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    link_direction: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LinkDirection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    link_projection: Optional[LinkProjectionStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
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
