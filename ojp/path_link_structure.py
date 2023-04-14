from dataclasses import dataclass, field
from typing import Optional
from ojp.access_feature_type_enumeration import AccessFeatureTypeEnumeration
from ojp.transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PathLinkStructure:
    """
    [TMv6] a link within a PLACE of or between two PLACEs (that is STOP PLACEs,
    ACCESS SPACEs or QUAYs,BOARDING POSITIONs,, POINTs OF INTEREST etc or PATH
    JUNCTIONs) that represents a step in a possible route for pedestrians,
    cyclists or other out-of-vehicle passengers within or between a PLACE.

    :ivar transition: Whether path is up down or level .
    :ivar access_feature_type: Type of physical feature of PATH LINK.
    :ivar count: Number how often the access feature occurs in this
        PathLink
    """
    transition: Optional[TransitionEnumeration] = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    access_feature_type: Optional[AccessFeatureTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
