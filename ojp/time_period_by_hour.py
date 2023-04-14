from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime
from ojp.extension_type import ExtensionType
from ojp.time_period_of_day import TimePeriodOfDay

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class TimePeriodByHour(TimePeriodOfDay):
    start_time_of_period: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "startTimeOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    end_time_of_period: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "endTimeOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    time_period_by_hour_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "timePeriodByHourExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
