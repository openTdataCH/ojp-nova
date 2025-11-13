from dataclasses import dataclass, field
from typing import Optional

from ojp2.international_text_structure import InternationalTextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class FollowStructure:
    """
    :ivar follow_sign_name: Follow a sign.
    :ivar follow_road_name: Follow a road/route.
    :ivar follow_direction_name: Follow a direction.
    :ivar follow_exit: Follow an exit.
    """

    follow_sign_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "FollowSignName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    follow_road_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "FollowRoadName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    follow_direction_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "FollowDirectionName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    follow_exit: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "FollowExit",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
