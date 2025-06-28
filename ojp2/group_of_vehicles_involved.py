from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.vehicle_characteristics import VehicleCharacteristics
from ojp2.vehicle_status_enum import VehicleStatusEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class GroupOfVehiclesInvolved:
    number_of_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_status: Optional[VehicleStatusEnum] = field(
        default=None,
        metadata={
            "name": "vehicleStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    group_of_vehicles_involved_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfVehiclesInvolvedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
