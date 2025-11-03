from dataclasses import dataclass, field
from typing import Optional

from ojp2.destination import Destination
from ojp2.extension_type import ExtensionType
from ojp2.point_1 import Point1

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class PointDestination(Destination):
    point: Optional[Point1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    point_destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
