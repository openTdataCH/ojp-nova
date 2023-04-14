from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from ojp.weekday_type_enumeration import WeekdayTypeEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class WeekdayTimePeriodStructure:
    """
    [a specialisation of TIME BAND in TMv6] aggregation of TIME BAND and DAY OF
    WEEK (Time period on a weekday).

    :ivar weekday: [a specialisation of DAY OF WEEK in TMv6] enumeration
        of individual the seven DAYs OF WEEK, along with public holidays
    :ivar start_time: Start time of period.
    :ivar duration: Time duration of period.
    """
    weekday: List[WeekdayTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Weekday",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
