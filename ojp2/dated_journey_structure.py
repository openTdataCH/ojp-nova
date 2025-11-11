from dataclasses import dataclass, field
from typing import Optional

from ojp2.booking_arrangements_container_structure import (
    BookingArrangementsContainerStructure,
)
from ojp2.compound_train import CompoundTrain
from ojp2.conventional_modes_of_operation_enumeration import (
    ConventionalModesOfOperationEnumeration,
)
from ojp2.direction_ref_structure import DirectionRefStructure
from ojp2.general_attribute_structure import GeneralAttributeStructure
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.journey_ref import JourneyRef
from ojp2.journey_relations_structure import JourneyRelationsStructure
from ojp2.line_ref_structure import LineRefStructure
from ojp2.mode_structure import ModeStructure
from ojp2.occupancy_enumeration import OccupancyEnumeration
from ojp2.operating_day_ref import OperatingDayRef
from ojp2.operator_ref_structure import OperatorRefStructure
from ojp2.operator_refs_rel_structure import OperatorRefsRelStructure
from ojp2.product_category_ref_structure import ProductCategoryRefStructure
from ojp2.product_category_structure_2 import ProductCategoryStructure2
from ojp2.reservation_needed_enumeration import ReservationNeededEnumeration
from ojp2.service_feature_ref import ServiceFeatureRef
from ojp2.service_via_point_structure import ServiceViaPointStructure
from ojp2.situation_ref_list import SituationRefList
from ojp2.stop_point_ref_structure import StopPointRefStructure
from ojp2.train import Train
from ojp2.train_element import TrainElement
from ojp2.train_element_ref import TrainElementRef
from ojp2.vehicle_feature_ref_structure import VehicleFeatureRefStructure
from ojp2.vehicle_ref import VehicleRef

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class DatedJourneyStructure:
    """[equivalent to  DATED VEHICLE JOURNEY in TMv6]  passenger carrying VEHICLE
    JOURNEY for one specified DAY TYPE for which the pattern of working is in
    principle defined by a SERVICE JOURNEY PATTERN.

    DatedJourney details of a service include its operating days.

    :ivar conventional_mode_of_operation: MODE OF OPERATION for
        scheduled and flexible services (NeTEx).
    :ivar operating_day_ref: Reference to an OPERATING DAY.
    :ivar journey_ref:
    :ivar public_code: Public code of the SERVICE JOURNEY (same meaning
        as in NeTEx). Examples: "512", "S8" or "Circle Line" or "ICE
        488".
    :ivar line_ref: Line Reference.
    :ivar direction_ref: Direction Reference.
    :ivar mode: [a specialisation of MODE in TMv6] an extended range of
        VEHICLE MODEs, aggregating them with some SUBMODEs
    :ivar product_category: A product category for the service. This is
        a classification defined in NeTEx/SIRI used to identify groups
        of journeys with some special properties for marketing and fare
        products, e.g., "TE2" for SNCF or a special panorama train "PE"
        in Switzerland.
    :ivar published_service_name: Line name or service description as
        known to the public, e.g., "512", "S8" or "Circle Line" or "ICE
        488".
    :ivar train_number: Contains the TrainNumber from NeTEx (TRAIN
        NUMBER from Transmodel). If several TrainNumber types exist, use
        the commercial one. In some cases also non-train modes will use
        TrainNumber.
    :ivar vehicle_ref: Contains the Vehicle reference of the vehicle. In
        Transmodel this may be the VEHICLE id.
    :ivar operator_refs: References to the OPERATORS. Multiple OPERATORS
        in case a ContinuousLeg can be operated by more than one
        operator, especially in the ALTERNATIVE MODE OF OPERATION where
        there can be dozens of taxi companies and many free-floating
        sharing companies.
    :ivar route_description: Descriptive text for a route, e.g.,
        "Airport via City Centre".
    :ivar via: Via points of the service that may help identify the
        vehicle to the public (In Transmodel modelled as TRIP REQUEST
        PLACE.TRIP VIA PLACE.GoVia; it will also most probably be
        detailed as a VIA and associated DESTINATION DISPLAY in the
        ROUTE description).
    :ivar restricted: This flag is set if the service can only be used
        in a restricted way. For example, a specific ACCESS MODE is
        required (e.g., dragLift) or the LINE is only made available to
        certain passenger groups (e.g., school buses, hotel shuttles).
    :ivar restriction_note: Information about the restriction.
    :ivar attribute: Note or service attribute.
    :ivar origin_stop_point_ref: First stop of the vehicle journey;
        origin stop point.
    :ivar origin_text: Label for first stop.
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
    :ivar destination_stop_point_ref: Last stop of vehicle journey;
        destination stop point.
    :ivar destination_text: Label for last stop. Should be set for
        classic public transport. Demand responsive and newer modes of
        operation will often not have a destination text.
    :ivar unplanned: Whether this trip is an additional one that has not
        been planned. Default is false.
    :ivar cancelled: Whether this trip is cancelled and will not be run.
        Default is false.
    :ivar deviation: Whether this trip deviates from the planned service
        pattern. Default is false.
    :ivar undefined_delay: Whether this trip may have an undefined
        delay. Default is false. More details could be provided in a
        PtSituation.
    :ivar occupancy: [equivalent to OCCUPANCY in SIRI] passenger load
        status of a VEHICLE. If omitted, not known.
    :ivar journey_relations: Relations of the journey with other
        journeys, e.g., in case a joining/splitting takes place or the
        journey substitutes for another one etc.
    :ivar train_elements:
    :ivar trains:
    :ivar compound_trains:
    :ivar booking_arrangements: Container with information on booking
        possibilities for this service.
    :ivar reservation_needed: Indicates whether this service needs some
        kind of reservation or booking to run.
    :ivar situation_full_refs: A list of references to SITUATIONs.
    :ivar extension:
    """

    conventional_mode_of_operation: Optional[
        ConventionalModesOfOperationEnumeration
    ] = field(
        default=None,
        metadata={
            "name": "ConventionalModeOfOperation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    operating_day_ref: Optional[OperatingDayRef] = field(
        default=None,
        metadata={
            "name": "OperatingDayRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    journey_ref: Optional[JourneyRef] = field(
        default=None,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
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
    direction_ref: Optional[DirectionRefStructure] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    mode: Optional[ModeStructure] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    product_category: Optional[ProductCategoryStructure2] = field(
        default=None,
        metadata={
            "name": "ProductCategory",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    published_service_name: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "PublishedServiceName",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    train_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainNumber",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
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
    operator_refs: Optional[OperatorRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRefs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    route_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "RouteDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    via: list[ServiceViaPointStructure] = field(
        default_factory=list,
        metadata={
            "name": "Via",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Restricted",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    restriction_note: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "RestrictionNote",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    attribute: list[GeneralAttributeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    origin_stop_point_ref: Optional[StopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "OriginStopPointRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    origin_text: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "OriginText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
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
    destination_stop_point_ref: Optional[StopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "DestinationStopPointRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    destination_text: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "DestinationText",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    unplanned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Unplanned",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    cancelled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Cancelled",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    deviation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Deviation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    undefined_delay: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UndefinedDelay",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    occupancy: Optional[OccupancyEnumeration] = field(
        default=None,
        metadata={
            "name": "Occupancy",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    journey_relations: Optional[JourneyRelationsStructure] = field(
        default=None,
        metadata={
            "name": "JourneyRelations",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    train_elements: Optional["DatedJourneyStructure.TrainElements"] = field(
        default=None,
        metadata={
            "name": "TrainElements",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    trains: Optional["DatedJourneyStructure.Trains"] = field(
        default=None,
        metadata={
            "name": "Trains",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    compound_trains: Optional["DatedJourneyStructure.CompoundTrains"] = field(
        default=None,
        metadata={
            "name": "CompoundTrains",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    booking_arrangements: Optional[BookingArrangementsContainerStructure] = (
        field(
            default=None,
            metadata={
                "name": "BookingArrangements",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            },
        )
    )
    reservation_needed: Optional[ReservationNeededEnumeration] = field(
        default=None,
        metadata={
            "name": "ReservationNeeded",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    situation_full_refs: Optional[SituationRefList] = field(
        default=None,
        metadata={
            "name": "SituationFullRefs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
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
