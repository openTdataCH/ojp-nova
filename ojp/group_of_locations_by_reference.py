from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.group_of_locations import GroupOfLocations

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class GroupOfLocationsByReference(GroupOfLocations):
    predefined_location_set_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    group_of_locations_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "groupOfLocationsByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
