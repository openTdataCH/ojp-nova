from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.day_week_month import DayWeekMonth
from ojp2.extension_type import ExtensionType
from ojp2.multilingual_string import MultilingualString
from ojp2.time_period_of_day import TimePeriodOfDay

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Period:
    start_of_period: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    end_of_period: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "endOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    period_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "periodName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    recurring_time_period_of_day: list[TimePeriodOfDay] = field(
        default_factory=list,
        metadata={
            "name": "recurringTimePeriodOfDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    recurring_day_week_month_period: list[DayWeekMonth] = field(
        default_factory=list,
        metadata={
            "name": "recurringDayWeekMonthPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    period_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "periodExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
