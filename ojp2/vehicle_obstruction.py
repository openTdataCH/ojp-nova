from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.obstruction import Obstruction
from ojp2.vehicle import Vehicle
from ojp2.vehicle_obstruction_type_enum import VehicleObstructionTypeEnum

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
        },
    )
    obstructing_vehicle: list[Vehicle] = field(
        default_factory=list,
        metadata={
            "name": "obstructingVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
