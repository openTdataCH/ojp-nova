from dataclasses import dataclass, field
from typing import Optional

from ojp2.block_ref_structure import BlockRefStructure
from ojp2.branding_ref_structure import BrandingRefStructure
from ojp2.branding_structure import BrandingStructure
from ojp2.compound_train import CompoundTrain
from ojp2.course_of_journey_ref_structure import CourseOfJourneyRefStructure
from ojp2.dated_call import DatedCall
from ojp2.dated_journey_part_info_structure import (
    DatedJourneyPartInfoStructure,
)
from ojp2.destination_ref import DestinationRef
from ojp2.extensions_2 import Extensions2
from ojp2.first_or_last_journey_enumeration import (
    FirstOrLastJourneyEnumeration,
)
from ojp2.framed_vehicle_journey_ref_structure import (
    FramedVehicleJourneyRefStructure,
)
from ojp2.group_of_lines_ref_structure import GroupOfLinesRefStructure
from ojp2.journey_note import JourneyNote
from ojp2.journey_pattern_ref_structure import JourneyPatternRefStructure
from ojp2.journey_relations_structure import JourneyRelationsStructure
from ojp2.line_ref_structure import LineRefStructure
from ojp2.natural_language_place_name_structure import (
    NaturalLanguagePlaceNameStructure,
)
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.operator_ref_structure import OperatorRefStructure
from ojp2.origin_ref import OriginRef
from ojp2.product_category_ref_structure import ProductCategoryRefStructure
from ojp2.published_line_name import PublishedLineName
from ojp2.route_ref_structure import RouteRefStructure
from ojp2.service_feature_ref import ServiceFeatureRef
from ojp2.simple_contact_structure import SimpleContactStructure
from ojp2.train import Train
from ojp2.train_block_part_structure import TrainBlockPartStructure
from ojp2.train_element import TrainElement
from ojp2.train_element_ref import TrainElementRef
from ojp2.train_number_ref_structure import TrainNumberRefStructure
from ojp2.vehicle_feature_ref_structure import VehicleFeatureRefStructure
from ojp2.vehicle_journey_ref import VehicleJourneyRef
from ojp2.vehicle_modes_enumeration import VehicleModesEnumeration
from ojp2.vehicle_ref import VehicleRef
from ojp2.via_name_structure import ViaNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DatedVehicleJourneyStructure:
    """
    Type for Planned VEHICLE JOURNEY (Production Timetable Service).

    :ivar dated_vehicle_journey_code: Identifier for a VEHICLE JOURNEY.
    :ivar framed_vehicle_journey_ref: Refecence to a VEHICLE JOURNEY
        framed by the day. SIRI 2.0
    :ivar vehicle_journey_ref:
    :ivar extra_journey: Whether this journey is an addition to the
        plan. Can only be used when both participants recognise the same
        schedule version. If omitted, defaults to false: the journey is
        not an addition.
    :ivar cancellation: Whether this journey is a cancellation of a
        journey in the plan. Can only be used when both participants
        recognise the same schedule version. If omitted, defaults to
        'false': the journey is not cancelled.
    :ivar journey_pattern_ref: Identifier of JOURNEY PATTERN that
        journey follows.
    :ivar journey_pattern_name: Name of Joruney Pattern
    :ivar vehicle_mode: A means of transportation such as bus, rail,
        etc.
    :ivar route_ref: Identifier of ROUTE that journey follows.
    :ivar published_line_name: Name or Number by which the LINE is known
        to the public.  (Unbounded since SIRI 2.0)
    :ivar group_of_lines_ref: Reference to a GROUP OF LINEs to which
        journey belongs. SIRI 2.0
    :ivar direction_name: Description of the DIRECTION. May correspond
        to a DESTINATION DISPLAY.  (Unbounded since SIRI 2.0)
    :ivar external_line_ref: Alternative identifier of LINE that an
        external system may associate with journey.
    :ivar branding_ref: Reference to a BRANDING. (since SIRI 2.1)
    :ivar branding: An arbitrary marketing classification. (since SIRI
        2.1)
    :ivar origin_ref:
    :ivar origin_name: Name of the origin of the journey.  (Unbounded
        since SIRI 2.0)
    :ivar origin_short_name: Short name of the origin of the journey;
        used to help identify the VEHICLE JOURNEY on arrival boards. If
        absent, same as Origin Name.
    :ivar destination_display_at_origin: DIRECTION name shown for jurney
        at the origin. (since SIRI 2.0)
    :ivar via: Names of VIA points, used to help identify the LINE, for
        example, Luton to Luton via Sutton. Currently 3 in VDV. Should
        only be included if the detail level was requested.
    :ivar destination_ref: Reference to a DESTINATION.
    :ivar destination_name: Description of the destination stop (vehicle
        signage), Can be overwritten for a journey, and then also
        section by section by the entry in an individual CALl.
        (Unbounded since SIRI 2.0)
    :ivar destination_short_name: Short name of the DESTINATION.of the
        journey; used to help identify the VEHICLE JOURNEY on arrival
        boards. If absent, same as DestinationName.  (Unbounded since
        SIRI 2.0)
    :ivar origin_display_at_destination: Origin name shown for jourey at
        the destination (since SIRI 2.0)
    :ivar operator_ref: OPERATOR of a VEHICLE JOURNEY.   Note that the
        operator may change over the course of a journey.  This shoudl
        show teh operator for the curent point in the journey.  Use
        Journey Parts tp record all the operators in the whole journeyh.
    :ivar product_category_ref: Product Classification of VEHICLE
        JOURNEY- subdivides a transport mode. e.g. express, loacl.
    :ivar service_feature_ref: Classification of service into arbitrary
        Service categories, e.g. school bus. Recommended SIRI values
        based on TPEG are given in SIRI documentation and enumerated in
        the siri_facilities package. Corresponds to NeTEX TYPE OF
        SERVICe.
    :ivar vehicle_feature_ref: Features of VEHICLE providing journey.
        Recommended SIRI values based on TPEG are given in SIRI
        documentation and enumerated in the siri_facilities package.
    :ivar vehicle_journey_name: For train services with named journeys.
        Train name, e.g. “West Coast Express”. If omitted: No train
        name. Inherited property.  (Unbounded since SIRI 2.0)
    :ivar journey_note:
    :ivar public_contact: Contact details for use by members of public.
        (since SIRI 2.0)
    :ivar operations_contact: Contact details for use by operational
        staff. (since SIRI 2.0)
    :ivar origin_display: Description of the origin stop (vehicle
        signage) to show on vehicle, Can be overwritten for a journey,
        and then also section by section by the entry in an Individual
        Call.  (since SIRI 2.0)
    :ivar destination_display: Description of the destination stop
        (vehicle signage) to show on vehicle, Can be overwritten for a
        journey, and then also section by section by the entry in an
        Individual Call.  (Unbounded since SIRI 2.0)
    :ivar line_note: Additional Text associated with LINE.  (Unbounded
        since SIRI 2.0)
    :ivar first_or_last_journey: Whether journey is first or last
        jouurney of day. (since SIRI 2.0)
    :ivar headway_service: Whether this is a Headway Service, that is,
        one shown as operating at a prescribed interval rather than to a
        fixed timetable.
    :ivar monitored: Whether VEHICLE JOURNEYs of LINE are normally
        monitored. Provides a default value for the Monitored element on
        individual journeys of the timetable.
    :ivar train_block_part: If a VEHICLE JOURNEY is a coupled journey,
        i.e. comprises several coupled BLOCKparts, there will be a
        separate delivery for each BLOCKp art and this element will
        indicate the vehicles that the journey part uses.
    :ivar block_ref: BLOCK that VEHICLE is running.
    :ivar course_of_journey_ref: COURSE OF JOURNEY ('Run') that VEHICLE
        is running.
    :ivar vehicle_ref:
    :ivar train_numbers: TRAIN NUMBERs for journey. (since SIRI 2.0)
    :ivar journey_parts: JOURNEY PARTs making up JOURNEY +SIRIv2.0 e.
    :ivar train_elements:
    :ivar trains:
    :ivar compound_trains:
    :ivar dated_calls: Complete sequence of stops along the route path,
        in calling order.
    :ivar journey_relations: Relations of the journey with other
        journeys, e.g., in case a joining/splitting takes place or the
        journey substitutes for another one etc.
    :ivar extensions:
    """

    dated_vehicle_journey_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
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
    vehicle_journey_ref: Optional[VehicleJourneyRef] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extra_journey: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExtraJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    cancellation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cancellation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_pattern_ref: Optional[JourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "JourneyPatternRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_pattern_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "JourneyPatternName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_mode: list[VehicleModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    route_ref: Optional[RouteRefStructure] = field(
        default=None,
        metadata={
            "name": "RouteRef",
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
    group_of_lines_ref: Optional[GroupOfLinesRefStructure] = field(
        default=None,
        metadata={
            "name": "GroupOfLinesRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    direction_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DirectionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    external_line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalLineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    branding_ref: Optional[BrandingRefStructure] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    branding: Optional[BrandingStructure] = field(
        default=None,
        metadata={
            "name": "Branding",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_ref: Optional[OriginRef] = field(
        default=None,
        metadata={
            "name": "OriginRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_name: list[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_short_name: list[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
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
    via: list[ViaNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "Via",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_ref: Optional[DestinationRef] = field(
        default=None,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_short_name: list[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationShortName",
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
    operator_ref: Optional[OperatorRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    product_category_ref: Optional[ProductCategoryRefStructure] = field(
        default=None,
        metadata={
            "name": "ProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_feature_ref: list[ServiceFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeatureRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_feature_ref: list[VehicleFeatureRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleFeatureRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_journey_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_note: list[JourneyNote] = field(
        default_factory=list,
        metadata={
            "name": "JourneyNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    public_contact: Optional[SimpleContactStructure] = field(
        default=None,
        metadata={
            "name": "PublicContact",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operations_contact: Optional[SimpleContactStructure] = field(
        default=None,
        metadata={
            "name": "OperationsContact",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_display: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginDisplay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_display: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_note: list[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "LineNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    first_or_last_journey: Optional[FirstOrLastJourneyEnumeration] = field(
        default=None,
        metadata={
            "name": "FirstOrLastJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    headway_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HeadwayService",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_block_part: list[TrainBlockPartStructure] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlockPart",
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
    course_of_journey_ref: Optional[CourseOfJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "CourseOfJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_numbers: Optional["DatedVehicleJourneyStructure.TrainNumbers"] = (
        field(
            default=None,
            metadata={
                "name": "TrainNumbers",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    journey_parts: Optional["DatedVehicleJourneyStructure.JourneyParts"] = (
        field(
            default=None,
            metadata={
                "name": "JourneyParts",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    train_elements: Optional["DatedVehicleJourneyStructure.TrainElements"] = (
        field(
            default=None,
            metadata={
                "name": "TrainElements",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    trains: Optional["DatedVehicleJourneyStructure.Trains"] = field(
        default=None,
        metadata={
            "name": "Trains",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    compound_trains: Optional[
        "DatedVehicleJourneyStructure.CompoundTrains"
    ] = field(
        default=None,
        metadata={
            "name": "CompoundTrains",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    dated_calls: Optional["DatedVehicleJourneyStructure.DatedCalls"] = field(
        default=None,
        metadata={
            "name": "DatedCalls",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    journey_relations: Optional[JourneyRelationsStructure] = field(
        default=None,
        metadata={
            "name": "JourneyRelations",
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
    class DatedCalls:
        dated_call: list[DatedCall] = field(
            default_factory=list,
            metadata={
                "name": "DatedCall",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 2,
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

        journey_part_info: list[DatedJourneyPartInfoStructure] = field(
            default_factory=list,
            metadata={
                "name": "JourneyPartInfo",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass
    class TrainElements:
        train_element_ref: list[TrainElementRef] = field(
            default_factory=list,
            metadata={
                "name": "TrainElementRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        train_element: list[TrainElement] = field(
            default_factory=list,
            metadata={
                "name": "TrainElement",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass
    class Trains:
        train_ref: list[object] = field(
            default_factory=list,
            metadata={
                "name": "TrainRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        train: list[Train] = field(
            default_factory=list,
            metadata={
                "name": "Train",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass
    class CompoundTrains:
        compound_train_ref: list[object] = field(
            default_factory=list,
            metadata={
                "name": "CompoundTrainRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        compound_train: list[CompoundTrain] = field(
            default_factory=list,
            metadata={
                "name": "CompoundTrain",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
