from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.overall_period import OverallPeriod
from ojp.validity_status_enum import ValidityStatusEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Validity:
    validity_status: Optional[ValidityStatusEnum] = field(
        default=None,
        metadata={
            "name": "validityStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    overrunning: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    validity_time_specification: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "validityTimeSpecification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    validity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "validityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
