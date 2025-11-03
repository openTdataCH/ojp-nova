from dataclasses import dataclass, field

from ojp2.days_of_week_enumerationx import DaysOfWeekEnumerationx
from ojp2.half_open_time_range_structure_2 import HalfOpenTimeRangeStructure2
from ojp2.half_open_timestamp_output_range_structure import (
    HalfOpenTimestampOutputRangeStructure,
)
from ojp2.holiday_type_enumerationx import HolidayTypeEnumerationx

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MonitoringValidityConditionStructure:
    """
    Allowed values for the type for Description of the monitoring conditions
    (frequency of mesurement, etc): an automatic monitoring of the status of a lift
    with pushed alert in case of incident is very different from a daily
    manual/visual check.

    :ivar period: Date and tme range within which condition is
        available.
    :ivar timeband: Monitoring period within a single day (monitoring
        may not be available at night, or may ony occur at certain time
        of day for manual monitoring, etc.). Several periods can be
        defined.
    :ivar day_type: Days type for monitoring availability.
    :ivar holiday_type: Holiday type for monitoring availability.
    """

    period: list[HalfOpenTimestampOutputRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    timeband: list[HalfOpenTimeRangeStructure2] = field(
        default_factory=list,
        metadata={
            "name": "Timeband",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    day_type: list[DaysOfWeekEnumerationx] = field(
        default_factory=list,
        metadata={
            "name": "DayType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    holiday_type: list[HolidayTypeEnumerationx] = field(
        default_factory=list,
        metadata={
            "name": "HolidayType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
