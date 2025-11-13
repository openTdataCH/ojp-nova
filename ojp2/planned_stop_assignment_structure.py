from dataclasses import dataclass, field
from typing import Optional

from ojp2.aimed_flexible_area import AimedFlexibleArea
from ojp2.aimed_flexible_area_ref import AimedFlexibleAreaRef
from ojp2.aimed_location_name import AimedLocationName
from ojp2.boarding_position_ref_structure_2 import (
    BoardingPositionRefStructure2,
)
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.quay_ref_structure_2 import QuayRefStructure2
from ojp2.quay_type import QuayType

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PlannedStopAssignmentStructure:
    """Type for assignment of a SCHEDULED STOP POINT to a physical location, in
    particular to a QUAY or BOARDING POSITION, according to the planned timetable.

    (since SIRI 2.0).

    :ivar aimed_quay_ref: Physical QUAY to use according to the planned
        timetable. (since SIRI 2.0)
    :ivar aimed_quay_name: Scheduled Platform name. (since SIRI 2.0)
    :ivar quay_type:
    :ivar aimed_boarding_position_ref: Physical BOARDING POSITION to use
        according to the planned timetable. (since SIRI 2.1)
    :ivar aimed_boarding_position_name: Scheduled BOARDING POSITION
        name. (since SIRI 2.1)
    :ivar aimed_flexible_area:
    :ivar aimed_flexible_area_ref:
    :ivar aimed_location_name:
    """

    aimed_quay_ref: Optional[QuayRefStructure2] = field(
        default=None,
        metadata={
            "name": "AimedQuayRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_quay_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "AimedQuayName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    quay_type: Optional[QuayType] = field(
        default=None,
        metadata={
            "name": "QuayType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_boarding_position_ref: Optional[BoardingPositionRefStructure2] = (
        field(
            default=None,
            metadata={
                "name": "AimedBoardingPositionRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    aimed_boarding_position_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "AimedBoardingPositionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_flexible_area: Optional[AimedFlexibleArea] = field(
        default=None,
        metadata={
            "name": "AimedFlexibleArea",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_flexible_area_ref: Optional[AimedFlexibleAreaRef] = field(
        default=None,
        metadata={
            "name": "AimedFlexibleAreaRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_location_name: list[AimedLocationName] = field(
        default_factory=list,
        metadata={
            "name": "AimedLocationName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
