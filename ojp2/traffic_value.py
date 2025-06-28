from dataclasses import dataclass, field
from typing import Optional

from ojp2.basic_data_value import BasicDataValue
from ojp2.extension_type import ExtensionType
from ojp2.vehicle_characteristics import VehicleCharacteristics

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TrafficValue(BasicDataValue):
    for_vehicles_with_characteristics_of: Optional[VehicleCharacteristics] = (
        field(
            default=None,
            metadata={
                "name": "forVehiclesWithCharacteristicsOf",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            },
        )
    )
    traffic_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
