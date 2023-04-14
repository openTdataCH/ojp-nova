from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from ojp.fare_class_enumeration import FareClassEnumeration
from ojp.group_reservation_structure import GroupReservationStructure
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.occupancy_enumeration import OccupancyEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VehicleOccupancyStructure:
    """Real-time occupancies of a VEHICLE (by fare class).

    Could be feedback from an automatic passenger counting system (APC)
    or estimated values from statistics. (since SIRI 2.1)

    :ivar compound_train_ref:
    :ivar train_ref:
    :ivar train_in_compound_train_ref:
    :ivar train_element_ref:
    :ivar train_component_ref:
    :ivar entrance_to_vehicle_ref:
    :ivar fare_class: Fare class in VEHICLE for which occupancy or
        capacities are specified.
    :ivar passenger_category: Adult, child, wheelchair etc.
    :ivar occupancy_level: An approximate figure of how occupied or full
        a VEHICLE and its parts are, e.g. 'manySeatsAvailable' or
        'standingRoomOnly'. More accurate data can be provided by the
        individual occupancies or capacities below.
    :ivar occupancy_percentage: Utilised percentage of maximum payload
        after departing the STOP POINT.
    :ivar alighting_count: Total number of alighting passengers for this
        vehicle journey at this STOP POINT.
    :ivar boarding_count: Total number of boarding passengers for this
        vehicle journey at this STOP POINT.
    :ivar onboard_count: Total number of passengers on-board after
        departing the STOP POINT.
    :ivar special_places_occupied: Total number of special places, e.g.
        seats for the disabled or lounge seats, that are occupied after
        departing the STOP POINT.
    :ivar pushchairs_onboard_count: Total number of pushchairs on-board
        after departing the STOP POINT.
    :ivar wheelchairs_onboard_count: Total number of wheelchairs on-
        board after departing the STOP POINT.
    :ivar prams_onboard_count: Total number of prams on-board after
        departing the STOP POINT.
    :ivar bicycle_onboard_count: Total number of bicycles on-board,
        i.e., number of bicycle racks that are occupied after departing
        the STOP POINT.
    :ivar total_number_of_reserved_seats: Total number of booked seats
        from individual and group reservations.
    :ivar group_reservation: Reservations of travel groups, i.e., name
        of group and number of seats booked.
    """
    compound_train_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    train_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    train_in_compound_train_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainInCompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    train_element_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    train_component_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    entrance_to_vehicle_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "EntranceToVehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    passenger_category: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "PassengerCategory",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    occupancy_level: Optional[OccupancyEnumeration] = field(
        default=None,
        metadata={
            "name": "OccupancyLevel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    occupancy_percentage: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "OccupancyPercentage",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_inclusive": Decimal("0"),
        }
    )
    alighting_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "AlightingCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    boarding_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "BoardingCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "OnboardCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    special_places_occupied: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpecialPlacesOccupied",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    pushchairs_onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PushchairsOnboardCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    wheelchairs_onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "WheelchairsOnboardCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    prams_onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PramsOnboardCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    bicycle_onboard_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "BicycleOnboardCount",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    total_number_of_reserved_seats: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfReservedSeats",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    group_reservation: List[GroupReservationStructure] = field(
        default_factory=list,
        metadata={
            "name": "GroupReservation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
