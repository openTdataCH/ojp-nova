from dataclasses import dataclass, field
from typing import Optional

from ojp2.basic_data_value import BasicDataValue
from ojp2.extension_type import ExtensionType
from ojp2.traffic_status_enum import TrafficStatusEnum
from ojp2.traffic_trend_type_enum import TrafficTrendTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TrafficStatusValue(BasicDataValue):
    traffic_status: Optional[TrafficStatusEnum] = field(
        default=None,
        metadata={
            "name": "trafficStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_trend_type: Optional[TrafficTrendTypeEnum] = field(
        default=None,
        metadata={
            "name": "trafficTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_status_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficStatusValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
