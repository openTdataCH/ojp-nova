from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Visibility:
    minimum_visibility_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "minimumVisibilityDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    visibility_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "visibilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
