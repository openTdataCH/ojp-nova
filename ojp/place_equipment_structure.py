from dataclasses import dataclass, field
from typing import Optional
from ojp.extensions_2 import Extensions2
from ojp.installed_equipment_structure import InstalledEquipmentStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class PlaceEquipmentStructure(InstalledEquipmentStructure):
    """
    Type for SITE EQUIPMENT.
    """
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
