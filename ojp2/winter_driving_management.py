from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.network_management import NetworkManagement
from ojp2.winter_equipment_management_type_enum import (
    WinterEquipmentManagementTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class WinterDrivingManagement(NetworkManagement):
    winter_equipment_management_type: Optional[
        WinterEquipmentManagementTypeEnum
    ] = field(
        default=None,
        metadata={
            "name": "winterEquipmentManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    winter_driving_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "winterDrivingManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
