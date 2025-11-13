from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

from ojp2.block_ref_structure import BlockRefStructure
from ojp2.branding_ref_structure import BrandingRefStructure
from ojp2.branding_structure import BrandingStructure
from ojp2.compound_train import CompoundTrain
from ojp2.course_of_journey_ref_structure import CourseOfJourneyRefStructure
from ojp2.destination_ref import DestinationRef
from ojp2.direction_ref_structure import DirectionRefStructure
from ojp2.facility_change_element import FacilityChangeElement
from ojp2.facility_condition_element import FacilityConditionElement
from ojp2.first_or_last_journey import FirstOrLastJourney
from ojp2.formation_condition import FormationCondition
from ojp2.framed_vehicle_journey_ref_structure import (
    FramedVehicleJourneyRefStructure,
)
from ojp2.group_of_lines_ref_structure import GroupOfLinesRefStructure
from ojp2.journey_note import JourneyNote
from ojp2.journey_part_info_structure import JourneyPartInfoStructure
from ojp2.journey_pattern_ref_structure import JourneyPatternRefStructure
from ojp2.line_ref_structure import LineRefStructure
from ojp2.location_structure import LocationStructure
from ojp2.monitored_call_structure import MonitoredCallStructure
from ojp2.natural_language_place_name_structure import (
    NaturalLanguagePlaceNameStructure,
)
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.occupancy import Occupancy
from ojp2.onward_calls_structure import OnwardCallsStructure
from ojp2.operator_ref_structure import OperatorRefStructure
from ojp2.origin_ref import OriginRef
from ojp2.prediction_inaccurate import PredictionInaccurate
from ojp2.prediction_inaccurate_reason import PredictionInaccurateReason
from ojp2.previous_calls_structure import PreviousCallsStructure
from ojp2.product_category_ref_structure import ProductCategoryRefStructure
from ojp2.progress_rate_enumeration import ProgressRateEnumeration
from ojp2.published_line_name import PublishedLineName
from ojp2.quality_index_enumeration import QualityIndexEnumeration
from ojp2.route_ref_structure import RouteRefStructure
from ojp2.service_feature_ref import ServiceFeatureRef
from ojp2.simple_contact_structure import SimpleContactStructure
from ojp2.situation_ref import SituationRef
from ojp2.train import Train
from ojp2.train_block_part_structure import TrainBlockPartStructure
from ojp2.train_element import TrainElement
from ojp2.train_element_ref import TrainElementRef
from ojp2.train_number_ref_structure import TrainNumberRefStructure
from ojp2.vehicle_feature_ref_structure import VehicleFeatureRefStructure
from ojp2.vehicle_journey_ref import VehicleJourneyRef
from ojp2.vehicle_modes_enumeration import VehicleModesEnumeration
from ojp2.vehicle_ref import VehicleRef
from ojp2.vehicle_status_enumeration import VehicleStatusEnumeration
from ojp2.via_name_structure import ViaNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MonitoredVehicleJourneyStructure:
    """
    Type for Monitored VEHICLE JOURNEY.

    :ivar line_ref: Reference to LINE of journey.
    :ivar direction_ref: Reference to DIRECTION of journey.
    :ivar framed_vehicle_journey_ref: A reference to the DATED VEHICLE
        JOURNEY that the VEHICLE is making, unique with the data horizon
        of the service.
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
    :ivar vehicle_journey_name: For train services with named journeys.
        Train name, e.g. “West Coast Express”. If omitted: No train
        name. Inherited property.  (Unbounded since SIRI 2.0)
    :ivar journey_note:
    :ivar public_contact: Contact details for use by members of public.
        (since SIRI 2.0)
    :ivar operations_contact: Contact details for use by operational
        staff. (since SIRI 2.0)
    :ivar headway_service: Whether this is a Headway Service, that is
        shown as operating at a prescribed interval rather than to a
        fixed timetable. Default is 'false'.
    :ivar origin_aimed_departure_time: Timetabled departure time from
        Origin.
    :ivar destination_aimed_arrival_time: Timetabled arrival time at
        Destination.
    :ivar first_or_last_journey:
    :ivar formation_condition: Information about a change of the
        formation (e.g. TRAIN composition) or changes of vehicles within
        the formation. (since SIRI 2.1)
    :ivar facility_condition_element: Information about a change of
        Equipment availability at stop or on vehicle that may affect
        access or use.
    :ivar facility_change_element:
    :ivar situation_ref:
    :ivar monitored: Whether there is real-time information available
        for journey. Default is 'true'. It is recommended to specify a
        MonitoringError if Monitored is set to 'false'.
    :ivar monitoring_error: If Monitored is 'false', a (list of)
        reason(s) for non-availability of real-time data. Examples are
        "GPS", "GPRS", "Radio" etc. MonitoringError must not be used if
        Monitored is omitted or set to 'true'.
    :ivar in_congestion: Whether the VEHICLE iis in traffic congestion.
        If not, present, not known.
    :ivar in_panic: Whether the panic alarm on the VEHICLE is activated.
        This may lead to indeterminate predictions. If absent, default
        is 'false'.
    :ivar prediction_inaccurate:
    :ivar prediction_inaccurate_reason:
    :ivar data_source: System originating real-time data. Can be used to
        make judgements of relative quality and accuracy compared to
        other feeds.
    :ivar confidence_level: Confidence QUALITY LEVEL of data. Default is
        'reliable'.
    :ivar vehicle_location: Current geospatial location of VEHICLE.
        Measured to front of vehicle.
    :ivar location_recorded_at_time: Time at which location was
        recorded. If not present assume that the recorded  at time on
        the containing delivery.
    :ivar bearing: Bearing in compass degrees in which VEHICLE is
        heading.
    :ivar progress_rate: Rate of progress of VEHICLE. Default is
        'normal'
    :ivar velocity: Velocity of VEHICLE. EIther actual speed or average
        speed may be used. (since SIRI 2.0)
    :ivar engine_on: Whether the engine of the vehicle is on. Default is
        'true' (since SIRI 2.0)
    :ivar occupancy:
    :ivar delay: Delay of VEHICLE against schedule, to a precision in
        seconds. Early times are shown as negative values.
    :ivar progress_status: An arbitrary textual  status description of
        the running of this VEHICLE JOURNEY.  (Unbounded 0:* since SIRI
        2.0)
    :ivar vehicle_status: An classification of the progress state of
        running of this VEHICLE JOURNEY. (since SIRI 2.0)
    :ivar train_block_part: If a VEHICLE JOURNEY is a coupled journey,
        i.e. comprises several coupled BLOCKparts, there will be a
        separate delivery for each BLOCKp art and this element will
        indicate the vehicles that the journey part uses.
    :ivar block_ref: BLOCK that VEHICLE is running.
    :ivar course_of_journey_ref: COURSE OF JOURNEY ('Run') that VEHICLE
        is running.
    :ivar vehicle_journey_ref:
    :ivar vehicle_ref:
    :ivar additional_vehicle_journey_ref: Refercence to other VEHICLE
        Journeys ((since SIRI 2.0))
    :ivar driver_ref: A reference to the DRIVER or Crew currently logged
        in to operate a monitored VEHICLE. May be omitted if real-time
        data is not available - i.e. it is timetabled data. (since SIRI
        2.0)
    :ivar driver_name: The name oo the Driver or Crew   (since SIRI 2.0)
    :ivar train_numbers: TRAIN NUMBERs for journey. (since SIRI 2.0)
    :ivar journey_parts: JOURNEY PARTs making up JOURNEY +SIRIv2.0 e.
    :ivar train_elements:
    :ivar trains:
    :ivar compound_trains:
    :ivar previous_calls: Information on stops called at previously,
        origin and all intermediate stops up to but not including the
        current stop, in order or visits. Should only be included if the
        detail level was requested.
    :ivar monitored_call: Monitored CALL at the current stop. For SIRI-
        SM this is the stop for which data is requested. For SIRI-VM
        this is the most recent stop visited by the VEHICLE.
    :ivar onward_calls: Information on CALLs at the intermediate stops
        beyond the current stop, up to and including the destination, in
        order of visits. Should only be included if the detail level was
        requested.
    :ivar is_complete_stop_sequence: Whether the above CALL sequence is
        complete, i.e. represents every CALL of the ROUTE and so can be
        used to replace a previous CALL sequence. Default is 'false'.
    """

    line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "LineRef",
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
    headway_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HeadwayService",
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
    first_or_last_journey: Optional[FirstOrLastJourney] = field(
        default=None,
        metadata={
            "name": "FirstOrLastJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    formation_condition: list[FormationCondition] = field(
        default_factory=list,
        metadata={
            "name": "FormationCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_condition_element: list[FacilityConditionElement] = field(
        default_factory=list,
        metadata={
            "name": "FacilityConditionElement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_change_element: Optional[FacilityChangeElement] = field(
        default=None,
        metadata={
            "name": "FacilityChangeElement",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    situation_ref: list[SituationRef] = field(
        default_factory=list,
        metadata={
            "name": "SituationRef",
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
    monitoring_error: list[str] = field(
        default_factory=list,
        metadata={
            "name": "MonitoringError",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        },
    )
    in_congestion: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InCongestion",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    in_panic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InPanic",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    prediction_inaccurate: Optional[PredictionInaccurate] = field(
        default=None,
        metadata={
            "name": "PredictionInaccurate",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    prediction_inaccurate_reason: Optional[PredictionInaccurateReason] = field(
        default=None,
        metadata={
            "name": "PredictionInaccurateReason",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "DataSource",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    confidence_level: Optional[QualityIndexEnumeration] = field(
        default=None,
        metadata={
            "name": "ConfidenceLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "VehicleLocation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    location_recorded_at_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LocationRecordedAtTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    bearing: Optional[float] = field(
        default=None,
        metadata={
            "name": "Bearing",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress_rate: Optional[ProgressRateEnumeration] = field(
        default=None,
        metadata={
            "name": "ProgressRate",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    velocity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Velocity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    engine_on: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EngineOn",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    occupancy: Optional[Occupancy] = field(
        default=None,
        metadata={
            "name": "Occupancy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delay: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress_status: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ProgressStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_status: Optional[VehicleStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleStatus",
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
    vehicle_journey_ref: Optional[VehicleJourneyRef] = field(
        default=None,
        metadata={
            "name": "VehicleJourneyRef",
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
    additional_vehicle_journey_ref: list[FramedVehicleJourneyRefStructure] = (
        field(
            default_factory=list,
            metadata={
                "name": "AdditionalVehicleJourneyRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    driver_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DriverRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    driver_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DriverName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_numbers: Optional[
        "MonitoredVehicleJourneyStructure.TrainNumbers"
    ] = field(
        default=None,
        metadata={
            "name": "TrainNumbers",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    journey_parts: Optional[
        "MonitoredVehicleJourneyStructure.JourneyParts"
    ] = field(
        default=None,
        metadata={
            "name": "JourneyParts",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_elements: Optional[
        "MonitoredVehicleJourneyStructure.TrainElements"
    ] = field(
        default=None,
        metadata={
            "name": "TrainElements",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    trains: Optional["MonitoredVehicleJourneyStructure.Trains"] = field(
        default=None,
        metadata={
            "name": "Trains",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    compound_trains: Optional[
        "MonitoredVehicleJourneyStructure.CompoundTrains"
    ] = field(
        default=None,
        metadata={
            "name": "CompoundTrains",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    previous_calls: Optional[PreviousCallsStructure] = field(
        default=None,
        metadata={
            "name": "PreviousCalls",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored_call: Optional[MonitoredCallStructure] = field(
        default=None,
        metadata={
            "name": "MonitoredCall",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    onward_calls: Optional[OnwardCallsStructure] = field(
        default=None,
        metadata={
            "name": "OnwardCalls",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    is_complete_stop_sequence: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsCompleteStopSequence",
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
