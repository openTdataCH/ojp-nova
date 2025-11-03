from dataclasses import dataclass, field
from typing import Optional

from ojp2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class FilterReference:
    delete_filter: Optional[bool] = field(
        default=None,
        metadata={
            "name": "deleteFilter",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    filter_operation_approved: Optional[bool] = field(
        default=None,
        metadata={
            "name": "filterOperationApproved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    key_filter_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyFilterReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    filter_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "filterReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
