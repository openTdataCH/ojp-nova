from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.multilingual_string import MultilingualString
from ojp2.predefined_location import PredefinedLocation

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class PredefinedLocationSet:
    predefined_location_set_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    predefined_location_set_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    predefined_location: list[PredefinedLocation] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    predefined_location_set_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "predefinedLocationSetExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
