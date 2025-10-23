from dataclasses import dataclass, field
from typing import List, Optional
from ojp.extension_type import ExtensionType
from ojp.header_information import HeaderInformation
from ojp.payload_publication import PayloadPublication
from ojp.predefined_location_set import PredefinedLocationSet

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
        }
    )
    predefined_location_set: List[PredefinedLocationSet] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocationSet",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        }
    )
    predefined_locations_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "predefinedLocationsPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
