from dataclasses import dataclass, field
from typing import Optional

from ojp2.day_enum import DayEnum
from ojp2.extension_type import ExtensionType
from ojp2.month_of_year_enum import MonthOfYearEnum
from ojp2.week_of_month_enum import WeekOfMonthEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class DayWeekMonth:
    applicable_day: list[DayEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 7,
        },
    )
    applicable_week: list[WeekOfMonthEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableWeek",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 5,
        },
    )
    applicable_month: list[MonthOfYearEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableMonth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 12,
        },
    )
    day_week_month_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "dayWeekMonthExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
