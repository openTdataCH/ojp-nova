from dataclasses import dataclass, field
from typing import Optional
from ojp.activity import Activity
from ojp.authority_operation_type_enum import AuthorityOperationTypeEnum
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class AuthorityOperation(Activity):
    authority_operation_type: Optional[AuthorityOperationTypeEnum] = field(
        default=None,
        metadata={
            "name": "authorityOperationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    authority_operation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "authorityOperationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
