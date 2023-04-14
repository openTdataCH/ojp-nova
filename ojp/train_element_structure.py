from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from ojp.facility_structure import FacilityStructure
from ojp.fare_class_enumeration import FareClassEnumeration
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.passenger_capacity_structure import PassengerCapacityStructure
from ojp.train_element_type_enumeration import TrainElementTypeEnumeration
from ojp.type_of_fuel_enumeration import TypeOfFuelEnumeration
from ojp.vehicle_feature import VehicleFeature

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainElementStructure:
    """Type for TRAIN ELEMENT.

    (since SIRI 2.1)

    :ivar train_element_code: Identifier for TRAIN ELEMENT.
    :ivar train_element_type: Type of TRAIN ELEMENT.
    :ivar vehicle_number: Denotes the official "registration number" of
        the vehicle or wagon/coach. In rail transport VEHICLE NUMBER
        would be equal to the 12-digit UIC wagon/coach number, possibly
        followed by other combinations of letters, e.g. by the UIC
        classification of railway coaches.
    :ivar fare_classes:
    :ivar name: Name of VEHICLE TYPE.
    :ivar short_name: Short Name of VEHICLE TYPE.
    :ivar description: Description of VEHICLE TYPE.
    :ivar private_code:
    :ivar reversing_direction: Whether vehicles of the type have a
        reversing direction.
    :ivar self_propelled: Whether vehicles of the type are self-
        propelled.
    :ivar type_of_fuel: The type of fuel used by a vehicle of the type.
    :ivar euro_class: Euroclass of the vehicle type. Corresponds to the
        12-digit European Identification Number (EIN).
    :ivar maximum_passenger_capacities: Break down of capacities by FARE
        CLASS, i.e., maximum number of passengers that TRAIN ELEMENT can
        carry.
    :ivar low_floor: Whether Vehicle is low floor to facilitate access
        by the mobility impaired.
    :ivar has_lift_or_ramp: Whether vehicle has lift or ramp to
        facilitate wheelchair access.
    :ivar has_hoist: Whether vehicle has hoist for wheelchair access.
    :ivar length: The length of a VEHICLE of the type.
    :ivar width: The width of a VEHICLE of the type.
    :ivar height: The length of a VEHICLE of the type.
    :ivar weight: The weight of a VEHICLE of the type.
    :ivar facilities: Facilities of VEHICLE TYPE.
    """
    train_element_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainElementCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    train_element_type: Optional[TrainElementTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TrainElementType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    vehicle_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "VehicleNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    fare_classes: List[FareClassEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FareClasses",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "tokens": True,
        }
    )
    name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    short_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    private_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    reversing_direction: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversingDirection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    self_propelled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelfPropelled",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    type_of_fuel: Optional[TypeOfFuelEnumeration] = field(
        default=None,
        metadata={
            "name": "TypeOfFuel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    euro_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "EuroClass",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    maximum_passenger_capacities: Optional["TrainElementStructure.MaximumPassengerCapacities"] = field(
        default=None,
        metadata={
            "name": "MaximumPassengerCapacities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    low_floor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    has_lift_or_ramp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasLiftOrRamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    has_hoist: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasHoist",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    facilities: Optional["TrainElementStructure.Facilities"] = field(
        default=None,
        metadata={
            "name": "Facilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass
    class MaximumPassengerCapacities:
        maximum_passenger_capacity: List[PassengerCapacityStructure] = field(
            default_factory=list,
            metadata={
                "name": "MaximumPassengerCapacity",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )

    @dataclass
    class Facilities:
        vehicle_feature: List[VehicleFeature] = field(
            default_factory=list,
            metadata={
                "name": "VehicleFeature",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "sequential": True,
            }
        )
        facility: List[FacilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "Facility",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "sequential": True,
            }
        )
        facility_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "FacilityRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "sequential": True,
            }
        )
