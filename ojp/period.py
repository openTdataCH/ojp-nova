from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from ojp.day_week_month import DayWeekMonth
from ojp.extension_type import ExtensionType
from ojp.multilingual_string import MultilingualString
from ojp.time_period_of_day import TimePeriodOfDay

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Period:
    start_of_period: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    end_of_period: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "endOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    period_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "periodName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    recurring_time_period_of_day: List[TimePeriodOfDay] = field(
        default_factory=list,
        metadata={
            "name": "recurringTimePeriodOfDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    recurring_day_week_month_period: List[DayWeekMonth] = field(
        default_factory=list,
        metadata={
            "name": "recurringDayWeekMonthPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
    period_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "periodExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
