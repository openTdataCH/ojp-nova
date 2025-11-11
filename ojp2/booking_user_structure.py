from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.booking_user_structure_cycling_profile import (
    BookingUserStructureCyclingProfile,
)
from ojp2.booking_user_structure_hiking_profile import (
    BookingUserStructureHikingProfile,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class BookingUserStructure:
    """
    Passenger(s) for whom the service needs to be booked.

    :ivar age: Age of the passenger on the day of travel.
    :ivar wheelchair_user: Passenger uses a wheelchair. Default is
        FALSE.
    :ivar walking_frame: Passenger uses a walking frame. Default is
        FALSE.
    :ivar walking_stick: Passenger uses a walking stick. Default is
        FALSE.
    :ivar walking_impaired: Passenger is (maybe temporarily) walking
        impaired. Default is FALSE.
    :ivar pram: Passenger has a pram with him/her. Default is FALSE.
    :ivar heavy_luggage: Passenger has got heavy luggage. Default is
        FALSE.
    :ivar visually_impaired: Passenger is visually impaired.
    :ivar hearing_impaired: Passenger is hearing impaired.
    :ivar reading_impaired: Passenger is reading impaired.
    :ivar no_single_step: The user is not able to pass over (or wants to
        avoid) single steps. Stairs and non-level entrances are not
        excluded.
    :ivar no_stairs: The user is not able to walk up/downstairs.
    :ivar no_escalator: The user is not able to use an escalator.
    :ivar no_elevator: The user is not able to use an elevator.
    :ivar no_ramp: The user is not able to use a ramp.
    :ivar no_sight: The user is not able to see.
    :ivar no_travelator: The user is not able to use a travelator.
    :ivar level_entrance: The user needs vehicles with level entrance
        between platform and vehicle.
    :ivar level_entrance_or_boarding_aid: The user needs vehicles with
        level entrance between platform and vehicle, an appropriate
        ramp, or assistance for boarding or alighting (for assisted and
        unassisted wheelchairs, or similar constraints).
    :ivar bike_transport: The user wants to carry a bike on public
        transport (could be extended in future to transporting big
        luggage / animals / etc.).
    :ivar walk_speed: Deviation from average walking speed in percent.
        100% percent is average speed. Less than 100 % slower, Greater
        than 150% faster.
    :ivar additional_transfer_time: Additional time added to all
        transfers (also to transfers between individual to public
        transport, not modelled in Transmodel).
    :ivar hiking_profile: Users hiking profile. The main element to
        control general walking behaviour is WalkSpeed (together with
        accessibility constraints). Note: explanations in German can be
        found here:
        https://akademie.alpinewelten.com/bergwandern/klassifizierung-
        von-wanderwegen
    :ivar cycling_profile: Cycling profile of the user (especially for
        sportive activities).
    :ivar boarding_assistance: Whether assistance is required for
        boarding. Could be offered by the driver or station staff.
        Default is FALSE.
    :ivar alighting_assistance: Whether assistance is required for
        alighting. Could be offered by the driver or station staff.
        Default is FALSE.
    """

    age: Optional[int] = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    wheelchair_user: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairUser",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    walking_frame: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WalkingFrame",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    walking_stick: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WalkingStick",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    walking_impaired: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WalkingImpaired",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    pram: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Pram",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    heavy_luggage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HeavyLuggage",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    visually_impaired: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VisuallyImpaired",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    hearing_impaired: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HearingImpaired",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    reading_impaired: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReadingImpaired",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_single_step: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoSingleStep",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_stairs: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoStairs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_escalator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoEscalator",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_elevator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoElevator",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_ramp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoRamp",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_sight: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoSight",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    no_travelator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NoTravelator",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    level_entrance: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LevelEntrance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    level_entrance_or_boarding_aid: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LevelEntranceOrBoardingAid",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    bike_transport: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BikeTransport",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    walk_speed: Optional[int] = field(
        default=None,
        metadata={
            "name": "WalkSpeed",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    additional_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "AdditionalTransferTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    hiking_profile: Optional[BookingUserStructureHikingProfile] = field(
        default=None,
        metadata={
            "name": "HikingProfile",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    cycling_profile: Optional[BookingUserStructureCyclingProfile] = field(
        default=None,
        metadata={
            "name": "CyclingProfile",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    boarding_assistance: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BoardingAssistance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    alighting_assistance: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AlightingAssistance",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
