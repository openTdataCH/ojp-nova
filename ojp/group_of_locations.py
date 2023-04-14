from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class GroupOfLocations:
    group_of_locations_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfLocationsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
