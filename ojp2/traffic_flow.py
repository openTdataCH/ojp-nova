from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.traffic_value import TrafficValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TrafficFlow(TrafficValue):
    axle_flow: Optional[int] = field(
        default=None,
        metadata={
            "name": "axleFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    pcu_flow: Optional[int] = field(
        default=None,
        metadata={
            "name": "pcuFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    percentage_long_vehicles: Optional[float] = field(
        default=None,
        metadata={
            "name": "percentageLongVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_flow: Optional[int] = field(
        default=None,
        metadata={
            "name": "vehicleFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_flow_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficFlowExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
