from dataclasses import dataclass, field
from typing import Optional
from ojp.fare_class_enumeration import FareClassEnumeration
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PassengerCapacityStructure:
    """Real-time capacities of a VEHICLE (by fare class), i.e., number of
    available seats.

    Alternative way to communicate occupancy measurements. (since SIRI
    2.1)

    :ivar compound_train_ref:
    :ivar train_ref:
    :ivar train_in_compound_train_ref:
    :ivar train_element_ref:
    :ivar train_component_ref:
    :ivar entrance_to_vehicle_ref:
    :ivar fare_class: Fare class in VEHICLE for which occupancy or
        capacities are specified.
    :ivar passenger_category: Adult, child, wheelchair etc.
    :ivar total_capacity: The total capacity of the vehicle in number of
        passengers.
    :ivar seating_capacity: The seating capacity of the vehicle in
        number of passengers.
    :ivar standing_capacity: The standing capacity of the vehicle in
        number of passengers.
    :ivar special_place_capacity: The number of special places on the
        vehicle, e.g. seats for the disabled or lounge seats.
    :ivar pushchair_capacity: The number of push chair places on the
        vehicle.
    :ivar wheelchair_place_capacity: The number of wheelchair places on
        the vehicle.
    :ivar pram_place_capacity: The number of places on the vehicle that
        are suitable for prams.
    :ivar bicycle_rack_capacity: The number of bicycle racks on the
        vehicle.
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
    total_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    seating_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SeatingCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    standing_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "StandingCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    special_place_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpecialPlaceCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    pushchair_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PushchairCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    wheelchair_place_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "WheelchairPlaceCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    pram_place_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PramPlaceCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    bicycle_rack_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "BicycleRackCapacity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
