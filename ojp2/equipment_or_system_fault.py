from dataclasses import dataclass, field
from typing import Optional

from ojp2.equipment_or_system_fault_type_enum import (
    EquipmentOrSystemFaultTypeEnum,
)
from ojp2.equipment_or_system_type_enum import EquipmentOrSystemTypeEnum
from ojp2.extension_type import ExtensionType
from ojp2.traffic_element import TrafficElement

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class EquipmentOrSystemFault(TrafficElement):
    equipment_or_system_fault_type: Optional[
        EquipmentOrSystemFaultTypeEnum
    ] = field(
        default=None,
        metadata={
            "name": "equipmentOrSystemFaultType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    faulty_equipment_or_system_type: Optional[EquipmentOrSystemTypeEnum] = (
        field(
            default=None,
            metadata={
                "name": "faultyEquipmentOrSystemType",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
                "required": True,
            },
        )
    )
    equipment_or_system_fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "equipmentOrSystemFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
