from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.mobility import Mobility
from ojp.traffic_element import TrafficElement

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Activity(TrafficElement):
    mobility_of_activity: Optional[Mobility] = field(
        default=None,
        metadata={
            "name": "mobilityOfActivity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    activity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "activityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
