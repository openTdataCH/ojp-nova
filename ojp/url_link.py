from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.multilingual_string import MultilingualString
from ojp.url_link_type_enum import UrlLinkTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class UrlLink:
    url_link_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "urlLinkAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    url_link_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "urlLinkDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    url_link_type: Optional[UrlLinkTypeEnum] = field(
        default=None,
        metadata={
            "name": "urlLinkType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    url_link_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "urlLinkExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
