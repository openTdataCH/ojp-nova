from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extension_type import ExtensionType
from ojp.obstruction import Obstruction
from ojp.vehicle import Vehicle
from ojp.vehicle_obstruction_type_enum import VehicleObstructionTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class VehicleObstruction(Obstruction):
    vehicle_obstruction_type: Optional[VehicleObstructionTypeEnum] = field(
        default=None,
        metadata={
            "name": "vehicleObstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    obstructing_vehicle: List[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "obstructingVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    vehicle_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
