from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.extension_type import ExtensionType
from ojp2.period import Period

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class OverallPeriod:
    overall_start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "overallStartTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    overall_end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "overallEndTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    valid_period: list[Period] = field(
        default_factory=list,
        metadata={
            "name": "validPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    exception_period: list[Period] = field(
        default_factory=list,
        metadata={
            "name": "exceptionPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    overall_period_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "overallPeriodExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
