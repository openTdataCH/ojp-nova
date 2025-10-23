from dataclasses import dataclass, field
from typing import Optional
from ojp.area import Area
from ojp.destination import Destination
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AreaDestination(Destination):
    area: Optional[Area] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    area_destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "areaDestinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
