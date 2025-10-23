from dataclasses import dataclass, field
from typing import Optional
from ojp.country_enum import CountryEnum
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class InternationalIdentifier:
    country: Optional[CountryEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    national_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "nationalIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    international_identifier_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "internationalIdentifierExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
