from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ojp.extension_type import ExtensionType
from ojp.international_identifier import InternationalIdentifier
from ojp.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class PayloadPublication:
    feed_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "feedDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    feed_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "feedType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        }
    )
    publication_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publicationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    publication_creator: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "publicationCreator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    payload_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "payloadPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
