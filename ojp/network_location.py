from dataclasses import dataclass, field
from typing import Optional
from ojp.destination import Destination
from ojp.extension_type import ExtensionType
from ojp.location import Location
from ojp.supplementary_positional_description import SupplementaryPositionalDescription

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class NetworkLocation(Location):
    supplementary_positional_description: Optional[SupplementaryPositionalDescription] = field(
        default=None,
        metadata={
            "name": "supplementaryPositionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    destination: Optional[Destination] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    network_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "networkLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
