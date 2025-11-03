from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.road_maintenance_type_enum import RoadMaintenanceTypeEnum
from ojp2.roadworks import Roadworks

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class MaintenanceWorks(Roadworks):
    road_maintenance_type: list[RoadMaintenanceTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "roadMaintenanceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    maintenance_works_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "maintenanceWorksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
