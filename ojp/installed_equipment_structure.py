from dataclasses import dataclass
from ojp.abstract_equipment_structure import AbstractEquipmentStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class InstalledEquipmentStructure(AbstractEquipmentStructure):
    """
    Type for INSTALLED EQUIPMENT.
    """
