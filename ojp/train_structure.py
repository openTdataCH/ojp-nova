from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from ojp.facility_structure import FacilityStructure
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.passenger_capacity_structure import PassengerCapacityStructure
from ojp.train_component import TrainComponent
from ojp.train_size_enumeration import TrainSizeEnumeration
from ojp.type_of_fuel_enumeration import TypeOfFuelEnumeration
from ojp.vehicle_feature import VehicleFeature

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TrainStructure:
    """Type for TRAIN.

    (since SIRI 2.1)

    :ivar train_code: Identifier for TRAIN.
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
    :ivar number_of_cars: Number of cars needed in TRAIN.
    :ivar train_size_type: Nature of TRAIN size, e.g "short", "long",
        "normal". Default is "normal".
    :ivar train_components: Ordered collection of TRAIN COMPONENTs
        making up the TRAIN.
    """
    train_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
    maximum_passenger_capacities: Optional["TrainStructure.MaximumPassengerCapacities"] = field(
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
    facilities: Optional["TrainStructure.Facilities"] = field(
        default=None,
        metadata={
            "name": "Facilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    number_of_cars: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfCars",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    train_size_type: Optional[TrainSizeEnumeration] = field(
        default=None,
        metadata={
            "name": "TrainSizeType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    train_components: Optional["TrainStructure.TrainComponents"] = field(
        default=None,
        metadata={
            "name": "TrainComponents",
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

    @dataclass
    class TrainComponents:
        train_component_ref: List[str] = field(
            default_factory=list,
            metadata={
                "name": "TrainComponentRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )
        train_component: List[TrainComponent] = field(
            default_factory=list,
            metadata={
                "name": "TrainComponent",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )
