from dataclasses import dataclass, field
from typing import Optional

from ojp2.accessibility_assessment_structure import (
    AccessibilityAssessmentStructure,
)
from ojp2.block_ref_structure import BlockRefStructure
from ojp2.course_of_journey_ref_structure import CourseOfJourneyRefStructure
from ojp2.extensions_2 import Extensions2
from ojp2.framed_vehicle_journey_ref_structure import (
    FramedVehicleJourneyRefStructure,
)
from ojp2.location_structure import LocationStructure
from ojp2.operator_ref_structure import OperatorRefStructure
from ojp2.product_category_ref_structure import ProductCategoryRefStructure
from ojp2.service_feature_ref import ServiceFeatureRef
from ojp2.train_block_part_structure import TrainBlockPartStructure
from ojp2.vehicle_feature_ref_structure import VehicleFeatureRefStructure
from ojp2.vehicle_ref_structure import VehicleRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AffectedVehicleStructure:
    """
    Type for information about a VEHICLE  affected by an SITUATION.

    :ivar vehicle_ref: Reference to a specific VEHICLE affected by an
        SITUATION.
    :ivar vehicle_registration_number_plate: Registration plate of
        VEHICLE
    :ivar phone_number: (Mobile) phone number on which the vehicle can
        be called
    :ivar ipaddress: Internet protocol address of the VEHICLE in form
        000.000.000.000
    :ivar radio_address: Radio address of the VEHICLE
    :ivar framed_vehicle_journey_ref: Reference to VEHICLE JOURNEY
        framed by the day which the VEHICLE is running.
    :ivar location: Location where the VEHICLE was when the situation
        arose
    :ivar current_location: Current Location of the VEHICLE
    :ivar accessibility_assessment: Current Accessibility assessment  of
        vehicle.
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
    :ivar train_block_part: If a VEHICLE JOURNEY is a coupled journey,
        i.e. comprises several coupled BLOCK PARTs, there will be a
        separate delivery for each BLOCK PART and this element will
        indicate the vehicles that the journey part uses.
    :ivar block_ref: BLOCK that VEHICLE is running.
    :ivar course_of_journey_ref: COURSE OF JOURNEY ('Run') that VEHICLE
        is running.
    :ivar in_congestion: Whether the VEHICLE is in traffic congestion.
        If not, present, not known.
    :ivar in_panic: Whether the panic alarm on the VEHICLE is activated.
        Default is 'false'.
    :ivar headway_service: Whether this is a Headway Service, that is
        shown as operating at a prescribed interval rather than to a
        fixed timetable. Default is 'false'.
    :ivar extensions:
    """

    vehicle_ref: Optional[VehicleRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    vehicle_registration_number_plate: list[str] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRegistrationNumberPlate",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    ipaddress: Optional[str] = field(
        default=None,
        metadata={
            "name": "IPAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    radio_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "RadioAddress",
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
    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    current_location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "CurrentLocation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
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
    headway_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HeadwayService",
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
