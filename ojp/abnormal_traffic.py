from dataclasses import dataclass, field
from typing import Optional
from ojp.abnormal_traffic_type_enum import AbnormalTrafficTypeEnum
from ojp.extension_type import ExtensionType
from ojp.relative_traffic_flow_enum import RelativeTrafficFlowEnum
from ojp.traffic_element import TrafficElement
from ojp.traffic_flow_characteristics_enum import TrafficFlowCharacteristicsEnum
from ojp.traffic_trend_type_enum import TrafficTrendTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AbnormalTraffic(TrafficElement):
    abnormal_traffic_type: Optional[AbnormalTrafficTypeEnum] = field(
        default=None,
        metadata={
            "name": "abnormalTrafficType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    number_of_vehicles_waiting: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVehiclesWaiting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    queue_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "queueLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    relative_traffic_flow: Optional[RelativeTrafficFlowEnum] = field(
        default=None,
        metadata={
            "name": "relativeTrafficFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    traffic_flow_characteristics: Optional[TrafficFlowCharacteristicsEnum] = field(
        default=None,
        metadata={
            "name": "trafficFlowCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    traffic_trend_type: Optional[TrafficTrendTypeEnum] = field(
        default=None,
        metadata={
            "name": "trafficTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    abnormal_traffic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "abnormalTrafficExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
