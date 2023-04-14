from dataclasses import dataclass, field
from typing import Optional
from ojp.type_of_fuel_enumeration import TypeOfFuelEnumeration
from ojp.type_of_value_structure import TypeOfValueStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TypeOfVehicleFuelStructure:
    """Classification of vehicle energy type.

    See Transmodel TypeOfFuel. (since SIRI 2.1)

    :ivar type_of_fuel: Values for vehicle fuel type. Use of 'other'
        requires the additional open ended OtherTypeOfFuel to be filled.
    :ivar other_type_of_fuel: An arbitrary vehicle fuel classification.
    """
    type_of_fuel: Optional[TypeOfFuelEnumeration] = field(
        default=None,
        metadata={
            "name": "TypeOfFuel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    other_type_of_fuel: Optional[TypeOfValueStructure] = field(
        default=None,
        metadata={
            "name": "OtherTypeOfFuel",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
