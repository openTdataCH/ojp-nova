from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class FilterExitManagement:
    filter_end: Optional[bool] = field(
        default=None,
        metadata={
            "name": "filterEnd",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    filter_out_of_range: Optional[bool] = field(
        default=None,
        metadata={
            "name": "filterOutOfRange",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    filter_exit_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "filterExitManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
