from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.accessibility_assessment_structure import (
    AccessibilityAssessmentStructure,
)
from ojp2.affected_call_structure import AffectedCallStructure
from ojp2.affected_facility_structure import AffectedFacilityStructure
from ojp2.affected_operator_structure import AffectedOperatorStructure
from ojp2.affected_stop_point_structure import (
    AffectedRouteStructure,
    AffectedStopPointStructure,
)
from ojp2.block_ref_structure import BlockRefStructure
from ojp2.dated_vehicle_journey_ref_structure import (
    DatedVehicleJourneyRefStructure,
)
from ojp2.direction_ref_structure import DirectionRefStructure
from ojp2.extensions_2 import Extensions2
from ojp2.framed_vehicle_journey_ref_structure import (
    FramedVehicleJourneyRefStructure,
)
from ojp2.journey_part_info_structure import JourneyPartInfoStructure
from ojp2.line_ref_structure import LineRefStructure
from ojp2.natural_language_place_name_structure import (
    NaturalLanguagePlaceNameStructure,
)
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.published_line_name import PublishedLineName
from ojp2.service_condition_enumeration import ServiceConditionEnumeration
from ojp2.train_number_ref_structure import TrainNumberRefStructure
from ojp2.vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedVehicleJourneyStructure:
    """
    Type for information about a VEHICLE JOURNEY affected by a SITUATION.

    :ivar framed_vehicle_journey_ref: Refercence to a VEHICLE JOURENY
        framed by the day. SIRI 2.0
    :ivar vehicle_journey_ref: DEPRECATED (SIRI 2.1) - use only
        FramedVehicleJourneyRef
    :ivar dated_vehicle_journey_ref: Reference to a specific DATED
        VEHICLE JOURNEY affected by a SITUATION.
    :ivar journey_name: Name of journey affected by a SITUATION.
        (Unbounded since SIRI 2.0)
    :ivar operator: OPERATOR of LINE affected by SITUATION.
    :ivar line_ref: Reference to the LINE of the journey  affected by an
        SITUATION.
    :ivar published_line_name:
    :ivar direction_ref: DIRECTION of LINE in which journey runs.
    :ivar block_ref: BLOCK which journey runs. (since SIRI 2.0)
    :ivar train_numbers: TRAIN NUMBERs for journey. (since SIRI 2.0)
    :ivar journey_parts: JOURNEY PARTs making up JOURNEY +SIRIv2.0 e.
    :ivar origins: Restricts the affected scope to the specified origins
        from which the LINE runs. [equivalent to pti15 1 start_point
        route_description_type]
    :ivar destinations: Restricts the affected scope to the specified
        DESTINATIONs
    :ivar route: ROUTE affected by the SITUATION.
    :ivar origin_aimed_departure_time: Timetabled departure tme  of
        journey from Origin.
    :ivar destination_aimed_arrival_time: Timetabled arrival time of
        journey at Destination.
    :ivar origin_display_at_destination: DESTINATION name shown for
        journey at the origin. Can be Used to identify journey for user.
        (since SIRI 2.0),
    :ivar destination_display_at_origin: DESTINATION name shown for
        journey at the origin.  Can be Used to identify journey for
        user. (since SIRI 2.0)
    :ivar accessibility_assessment: Accessibility Disruption status ofto
        JOURNEY, as affected by Situation.
    :ivar journey_condition: Status of service for this Vehicle Journey
        - TPEG value. Multiple Conditions can be valid at the same time.
        (since SIRI 2.0)
    :ivar calls: CALLs making up VEHICLE JOURNEY [equivalent to TPEG
        pti15 3 stop, 15_5 not-stopping, 15-6 temporary stop
        route_description_type]
    :ivar facilities: Facilities available for VEHICLE JOURNEY   (since
        SIRI 2.0)
    :ivar extensions:
    """

    framed_vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = (
        field(
            default=None,
            metadata={
                "name": "FramedVehicleJourneyRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    vehicle_journey_ref: list[VehicleJourneyRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    dated_vehicle_journey_ref: list[DatedVehicleJourneyRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "JourneyName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator: Optional[AffectedOperatorStructure] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    published_line_name: list[PublishedLineName] = field(
        default_factory=list,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    block_ref: Optional[BlockRefStructure] = field(
        default=None,
        metadata={
            "name": "BlockRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_numbers: Optional["AffectedVehicleJourneyStructure.TrainNumbers"] = (
        field(
            default=None,
            metadata={
                "name": "TrainNumbers",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    journey_parts: Optional["AffectedVehicleJourneyStructure.JourneyParts"] = (
        field(
            default=None,
            metadata={
                "name": "JourneyParts",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    origins: list[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Origins",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destinations: list[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Destinations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    route: list[AffectedRouteStructure] = field(
        default_factory=list,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OriginAimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_aimed_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DestinationAimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_display_at_destination: list[NaturalLanguagePlaceNameStructure] = (
        field(
            default_factory=list,
            metadata={
                "name": "OriginDisplayAtDestination",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    destination_display_at_origin: list[NaturalLanguagePlaceNameStructure] = (
        field(
            default_factory=list,
            metadata={
                "name": "DestinationDisplayAtOrigin",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
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
    journey_condition: list[ServiceConditionEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "JourneyCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    calls: Optional["AffectedVehicleJourneyStructure.Calls"] = field(
        default=None,
        metadata={
            "name": "Calls",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facilities: Optional["AffectedVehicleJourneyStructure.Facilities"] = field(
        default=None,
        metadata={
            "name": "Facilities",
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

    @dataclass
    class TrainNumbers:
        """
        :ivar train_number_ref: TRAIN NUMBER  assigned to VEHICLE
            JOURNEY.  +SIRI  2.0
        """

        train_number_ref: list[TrainNumberRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "TrainNumberRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class JourneyParts:
        """
        :ivar journey_part_info: Information about Parts of JOURNEY
            (since SIRI 2.0)
        """

        journey_part_info: list[JourneyPartInfoStructure] = field(
            default_factory=list,
            metadata={
                "name": "JourneyPartInfo",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Calls:
        call: list[AffectedCallStructure] = field(
            default_factory=list,
            metadata={
                "name": "Call",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class Facilities:
        """
        :ivar affected_facility: Facililitiy available for VEHICLE
            JOURNEY   (since SIRI 2.0)
        """

        affected_facility: list[AffectedFacilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedFacility",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
