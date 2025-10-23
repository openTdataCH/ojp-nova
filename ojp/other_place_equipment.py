from dataclasses import dataclass
from ojp.place_equipment_structure import PlaceEquipmentStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass
class OtherPlaceEquipment(PlaceEquipmentStructure):
    """EQUIPMENT.

    that may be in a fixed within a SITe.
    """
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
