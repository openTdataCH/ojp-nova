from dataclasses import dataclass, field
from typing import Optional

from ojp2.access_feature_status_enumeration import (
    AccessFeatureStatusEnumeration,
)
from ojp2.access_feature_type_enumeration import AccessFeatureTypeEnumeration
from ojp2.accessibility_feature_types_enumeration import (
    AccessibilityFeatureTypesEnumeration,
)
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.path_link_end_structure import PathLinkEndStructure
from ojp2.situation_full_ref_2 import SituationFullRef2
from ojp2.transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PathLinkStructure:
    """[TMv6] a link within a PLACE of or between two PLACEs (that is STOP PLACEs,
    ACCESS SPACEs or QUAYs, BOARDING POSITIONs, POINTs OF INTEREST etc.

    or PATH JUNCTIONs) that represents a step in a possible route for
    pedestrians, cyclists, or other out-of-vehicle passengers within or
    between a PLACE. Here we use a reduced form of a PATH LINK
    containing the description of the type of accessibility on this
    navigation section.

    :ivar transition: Whether path is up, down, or level.
    :ivar access_feature_type: Type of physical feature of PATH LINK.
    :ivar count: Number indicating how often the access feature occurs
        in this PathLink
    :ivar access_feature_status: Whether the access feature is available
        or out of service.
    :ivar access_feature_status_text: Textual information about reduced
        availability of the access feature, in particular if
        AccessFeatureStatus is partiallyAvailable.
    :ivar accessibility_feature: Presence of an accessibility feature on
        the PathLink.
    :ivar situation_full_ref: Reference to a situation that affects the
        availability of the access feature.
    :ivar from_value: Designations of level and place where this
        PathLink starts.
    :ivar to: Designations of level and place where this PathLink ends.
    """

    transition: Optional[TransitionEnumeration] = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    access_feature_type: Optional[AccessFeatureTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    access_feature_status: Optional[AccessFeatureStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessFeatureStatus",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    access_feature_status_text: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "AccessFeatureStatusText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    accessibility_feature: list[AccessibilityFeatureTypesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityFeature",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    situation_full_ref: list[SituationFullRef2] = field(
        default_factory=list,
        metadata={
            "name": "SituationFullRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    from_value: Optional[PathLinkEndStructure] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    to: Optional[PathLinkEndStructure] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
