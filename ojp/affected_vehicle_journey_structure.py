from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from ojp.accessibility_assessment_structure import AccessibilityAssessmentStructure
from ojp.affected_call_structure import AffectedCallStructure
from ojp.affected_facility_structure import AffectedFacilityStructure
from ojp.affected_operator_structure import AffectedOperatorStructure
from ojp.affected_route_structure import AffectedRouteStructure
from ojp.affected_stop_point_structure import AffectedStopPointStructure
from ojp.extensions_1 import Extensions1
from ojp.framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure
from ojp.journey_part_info_structure import JourneyPartInfoStructure
from ojp.natural_language_place_name_structure import NaturalLanguagePlaceNameStructure
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.published_line_name import PublishedLineName
from ojp.service_condition_enumeration import ServiceConditionEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedVehicleJourneyStructure:
    """
    Type for information about a VEHICLE JOURNEY affected by a SITUATION.

    :ivar framed_vehicle_journey_ref: Refercence to a VEHICLE JOURENY
        framed by the day. SIRI 2.0
    :ivar vehicle_journey_ref: Reference to a service VEHICLE JOURNEY
        affected by a SITUATION.
    :ivar dated_vehicle_journey_ref: Reference to a specific DATED
        VEHICLE JOURNEY affected by a SITUATION.
    :ivar journey_name: Name of journey affected by a SITUATION.
        (Unbounded since SIRI 2.0)
    :ivar operator: OPERATOR of LINE affected by SITUATION.
    :ivar line_ref: Reference to the LINE of the journey  affected by an
        SITUATION.
    :ivar published_line_name:
    :ivar direction_ref: DIRECTION of LINE in which journey runs.
    :ivar block_ref: BLOCK which journey runs. +SIRI 2.0
    :ivar train_numbers: TRAIN NUMBERs for journey. +SIRI v2.0
    :ivar journey_parts: JOURNEY PARTs making up JOURNEY +SIRIv2.0 e.
    :ivar origins: Origin SCHEDULED STOP POINTs from which the LINE
        runs. [equivalent to pti15 1 start_point route_description_type]
    :ivar destinations: Destination SCHEDULED STOP POINTs  to which the
        LINE runs. [equivalent to pti15 2 destination
        route_description_type]
    :ivar route: ROUTE affected by the SITUATION.
    :ivar origin_aimed_departure_time: Timetabled departure tme  of
        journey from Origin.
    :ivar destination_aimed_arrival_time: Timetabled arrival time of
        journey at Destination.
    :ivar origin_display_at_destination: DESTINATION name shown for
        journey at the origin. Can be Used to identify joruney for user.
        (+SIRI 2.0),
    :ivar destination_display_at_origin: DESTINATION name shown for
        journey at the origin.  Can be Used to identify joruney for
        user. (+SIRI 2.0)
    :ivar accessibility_assessment: Accessibility Disruption status ofto
        JOURNEY, as affected by Situation.
    :ivar journey_condition: enum   Status of service for this Vehicle
        Journey - TPEG value. Multiple Condtions can be valid at the
        same time.  (+SIRI 2.0)
    :ivar calls: CALLs making up VEHICLE JOURNEY [equivalent to TPEG
        pti15 3 stop, 15_5 not-stopping, 15-6 temporary stop
        route_description_type]
    :ivar facilities: Facilities available for VEHICLE JOURNEY   (+SIRI
        2.0)
    :ivar extensions:
    """
    framed_vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FramedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    vehicle_journey_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    dated_vehicle_journey_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    journey_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "JourneyName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    operator: Optional[AffectedOperatorStructure] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    line_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    published_line_name: Optional[PublishedLineName] = field(
        default=None,
        metadata={
            "name": "PublishedLineName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    direction_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    block_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "BlockRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    train_numbers: Optional["AffectedVehicleJourneyStructure.TrainNumbers"] = field(
        default=None,
        metadata={
            "name": "TrainNumbers",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    journey_parts: Optional["AffectedVehicleJourneyStructure.JourneyParts"] = field(
        default=None,
        metadata={
            "name": "JourneyParts",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    origins: List[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Origins",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    destinations: List[AffectedStopPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Destinations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    route: List[AffectedRouteStructure] = field(
        default_factory=list,
        metadata={
            "name": "Route",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
    origin_aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "OriginAimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    destination_aimed_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "DestinationAimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    origin_display_at_destination: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginDisplayAtDestination",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    destination_display_at_origin: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayAtOrigin",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    journey_condition: List[ServiceConditionEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "JourneyCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    calls: Optional["AffectedVehicleJourneyStructure.Calls"] = field(
        default=None,
        metadata={
            "name": "Calls",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    facilities: Optional["AffectedVehicleJourneyStructure.Facilities"] = field(
        default=None,
        metadata={
            "name": "Facilities",
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

    @dataclass
    class TrainNumbers:
        """
        :ivar train_number_ref: TRAIN NUMBER  assigned to VEHICLE
            JOURNEY.  +SIRI  2.0
        """
        train_number_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "TrainNumberRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )

    @dataclass
    class JourneyParts:
        """
        :ivar journey_part_info: Information about Parts of JOURNEY
            +SIRI v2.0
        """
        journey_part_info: List[JourneyPartInfoStructure] = field(
            default_factory=list,
            metadata={
                "name": "JourneyPartInfo",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Calls:
        call: List[AffectedCallStructure] = field(
            default_factory=list,
            metadata={
                "name": "Call",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Facilities:
        """
        :ivar affected_facility: Facililitiy available for VEHICLE
            JOURNEY   (+SIRI 2.0)
        """
        affected_facility: List[AffectedFacilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedFacility",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )
