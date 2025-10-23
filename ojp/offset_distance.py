from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class OffsetDistance:
    offset_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    offset_distance_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "offsetDistanceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
