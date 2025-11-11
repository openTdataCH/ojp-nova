from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType
from ojp2.header_information import HeaderInformation
from ojp2.payload_publication import PayloadPublication
from ojp2.predefined_location_set import PredefinedLocationSet

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class PredefinedLocationsPublication(PayloadPublication):
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    predefined_location_set: list[PredefinedLocationSet] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocationSet",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    predefined_locations_publication_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "predefinedLocationsPublicationExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            },
        )
    )
