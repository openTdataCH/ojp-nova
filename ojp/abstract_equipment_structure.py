from dataclasses import dataclass, field
from typing import Optional
from ojp.data_managed_object_structure import DataManagedObjectStructure
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class AbstractEquipmentStructure(DataManagedObjectStructure):
    """
    Type for abstract EQUIPMENT.

    :ivar equipment_id: Identifer of EQUIPMENT.
    :ivar equipment_name: Name of EQUIPMENT.
    :ivar type_of_equipment: Type for reference to TYPE OF EQUIPMENT.
    """
    equipment_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "EquipmentId",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "required": True,
        }
    )
    equipment_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "EquipmentName",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
    type_of_equipment: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOfEquipment",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
