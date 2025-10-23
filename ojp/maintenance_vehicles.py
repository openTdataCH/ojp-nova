from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extension_type import ExtensionType
from ojp.maintenance_vehicle_actions_enum import MaintenanceVehicleActionsEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class MaintenanceVehicles:
    number_of_maintenance_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfMaintenanceVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    maintenance_vehicle_actions: List[MaintenanceVehicleActionsEnum] = field(
        default_factory=list,
        metadata={
            "name": "maintenanceVehicleActions",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    maintenance_vehicles_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "maintenanceVehiclesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
