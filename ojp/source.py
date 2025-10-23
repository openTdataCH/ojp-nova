from dataclasses import dataclass, field
from typing import Optional
from ojp.country_enum import CountryEnum
from ojp.extension_type import ExtensionType
from ojp.multilingual_string import MultilingualString
from ojp.source_type_enum import SourceTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Source:
    source_country: Optional[CountryEnum] = field(
        default=None,
        metadata={
            "name": "sourceCountry",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    source_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        }
    )
    source_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "sourceName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    source_type: Optional[SourceTypeEnum] = field(
        default=None,
        metadata={
            "name": "sourceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    reliable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    source_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "sourceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
