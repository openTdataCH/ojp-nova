from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.location import Location
from ojp2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class PredefinedLocation:
    predefined_location_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "predefinedLocationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    predefined_location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "predefinedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    predefined_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "predefinedLocationExtension",
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
