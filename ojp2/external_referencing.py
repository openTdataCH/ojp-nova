from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class ExternalReferencing:
    external_location_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalLocationCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    external_referencing_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalReferencingSystem",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    external_referencing_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "externalReferencingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
