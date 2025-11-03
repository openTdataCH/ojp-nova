from dataclasses import dataclass, field
from typing import Optional

from ojp2.aimed_flexible_area import AimedFlexibleArea
from ojp2.aimed_flexible_area_ref import AimedFlexibleAreaRef
from ojp2.aimed_location_name import AimedLocationName
from ojp2.boarding_position_ref_structure_2 import (
    BoardingPositionRefStructure2,
)
from ojp2.flexible_area_ref_structure import FlexibleAreaRefStructure
from ojp2.flexible_area_structure import FlexibleAreaStructure
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.quay_ref_structure_2 import QuayRefStructure2
from ojp2.quay_type import QuayType

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class StopAssignmentStructure:
    """Type for assignment of a SCHEDULED STOP POINT to a physical location, in
    particular to a QUAY or BOARDING POSITION.

    (since SIRI 2.0).

    :ivar aimed_quay_ref: Physical QUAY to use according to the planned
        timetable. (since SIRI 2.0)
    :ivar aimed_quay_name: Scheduled Platform name. Can be used to
        indicate platfrom change. (since SIRI 2.0)
    :ivar expected_quay_ref: Physical QUAY to use according to the real-
        time prediction. (since SIRI 2.0)
    :ivar expected_quay_name: Expected Platform name. Can be used to
        indicate real-time prediction. (since SIRI 2.1)
    :ivar actual_quay_ref: Physical QUAY actually used. (since SIRI 2.0)
    :ivar actual_quay_name: Actual Platform name. Can be used to
        indicate recorded platform. (since SIRI 2.1)
    :ivar quay_type:
    :ivar aimed_boarding_position_ref: Physical BOARDING POSITION to use
        according to the planned timetable.
    :ivar aimed_boarding_position_name: Scheduled BOARDING POSITION
        name. Can be used to indicate boarding position change.
    :ivar expected_boarding_position_ref: Physical BOARDING POSITION to
        use according to the real-time prediction.
    :ivar expected_boarding_position_name: Expected BOARDING POSITION
        name. Can be used to indicate real-time prediction.
    :ivar actual_boarding_position_ref: Actually recorded BOARDING
        POSITION. Can be used to indicate the actually used boarding
        position.
    :ivar actual_boarding_position_name: Recorded BOARDING POSITION
        name. Can be used to indicate the actually used boarding
        position.
    :ivar aimed_flexible_area:
    :ivar aimed_flexible_area_ref:
    :ivar aimed_location_name:
    :ivar expected_flexible_area: Area that encompasses the expected
        flexible stop locations according to the real-time prediction.
    :ivar expected_flexible_area_ref:
    :ivar expected_location_name: Name or description (e.g. address) of
        the expected location or flexible area.
    :ivar actual_flexible_area: Area that encompasses the actually
        recorded flexible stop locations.
    :ivar actual_flexible_area_ref:
    :ivar actual_location_name: Name or description (e.g. address) of
        the actually recorded location or flexible area.
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
    expected_quay_ref: Optional[QuayRefStructure2] = field(
        default=None,
        metadata={
            "name": "ExpectedQuayRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_quay_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ExpectedQuayName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_quay_ref: Optional[QuayRefStructure2] = field(
        default=None,
        metadata={
            "name": "ActualQuayRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_quay_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ActualQuayName",
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
    expected_boarding_position_ref: Optional[BoardingPositionRefStructure2] = (
        field(
            default=None,
            metadata={
                "name": "ExpectedBoardingPositionRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    expected_boarding_position_name: list[NaturalLanguageStringStructure] = (
        field(
            default_factory=list,
            metadata={
                "name": "ExpectedBoardingPositionName",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    actual_boarding_position_ref: Optional[BoardingPositionRefStructure2] = (
        field(
            default=None,
            metadata={
                "name": "ActualBoardingPositionRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    actual_boarding_position_name: list[NaturalLanguageStringStructure] = (
        field(
            default_factory=list,
            metadata={
                "name": "ActualBoardingPositionName",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
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
    expected_flexible_area: Optional[FlexibleAreaStructure] = field(
        default=None,
        metadata={
            "name": "ExpectedFlexibleArea",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_flexible_area_ref: Optional[FlexibleAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "ExpectedFlexibleAreaRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_location_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ExpectedLocationName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_flexible_area: Optional[FlexibleAreaStructure] = field(
        default=None,
        metadata={
            "name": "ActualFlexibleArea",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_flexible_area_ref: Optional[FlexibleAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "ActualFlexibleAreaRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_location_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ActualLocationName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
