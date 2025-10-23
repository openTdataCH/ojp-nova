from dataclasses import dataclass, field
from typing import Optional
from ojp.destination import Destination
from ojp.extension_type import ExtensionType
from ojp.point import Point

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class PointDestination(Destination):
    point: Optional[Point] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    point_destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pointDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
