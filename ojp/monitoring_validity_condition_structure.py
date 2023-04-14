from dataclasses import dataclass, field
from typing import List
from ojp.days_of_week_enumerationx import DaysOfWeekEnumerationx
from ojp.half_open_time_range_structure_1 import HalfOpenTimeRangeStructure1
from ojp.half_open_timestamp_output_range_structure import HalfOpenTimestampOutputRangeStructure
from ojp.holiday_type_enumerationx import HolidayTypeEnumerationx

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class MonitoringValidityConditionStructure:
    """
    Allowed values for the type for Description of the monitoring conditions
    (frequency of mesurement, etc): an automatic monitoring of the satus of a
    lift with pushed alert in case of incident is very different from a daily
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
    period: List[HalfOpenTimestampOutputRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    timeband: List[HalfOpenTimeRangeStructure1] = field(
        default_factory=list,
        metadata={
            "name": "Timeband",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    day_type: List[DaysOfWeekEnumerationx] = field(
        default_factory=list,
        metadata={
            "name": "DayType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    holiday_type: List[HolidayTypeEnumerationx] = field(
        default_factory=list,
        metadata={
            "name": "HolidayType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
