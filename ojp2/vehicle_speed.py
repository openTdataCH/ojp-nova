from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class VehicleSpeed:
    individual_vehicle_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "individualVehicleSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    vehicle_speed_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vehicleSpeedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
