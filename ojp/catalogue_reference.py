from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class CatalogueReference:
    key_catalogue_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyCatalogueReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    catalogue_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "catalogueReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
