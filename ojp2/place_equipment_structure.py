from dataclasses import dataclass, field
from typing import Optional

from ojp2.extensions_1 import Extensions1
from ojp2.installed_equipment_structure import InstalledEquipmentStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class PlaceEquipmentStructure(InstalledEquipmentStructure):
    """
    Type for SITE EQUIPMENT.
    """

    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
