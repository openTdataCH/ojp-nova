from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.mobility import Mobility
from ojp2.traffic_element import TrafficElement

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Obstruction(TrafficElement):
    number_of_obstructions: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfObstructions",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    mobility_of_obstruction: Optional[Mobility] = field(
        default=None,
        metadata={
            "name": "mobilityOfObstruction",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "obstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
