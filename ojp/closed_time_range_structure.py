from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime
from ojp.end_time_precision_enumeration import EndTimePrecisionEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ClosedTimeRangeStructure:
    """Type for a range of times.

    Both start and end time are required.

    :ivar start_time: The (inclusive) start time.
    :ivar end_time: The (inclusive) end time.
    :ivar end_time_precision: Precision with which to interpret the
        inclusive end time. Default is to the second.
    """
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    end_time_precision: Optional[EndTimePrecisionEnumeration] = field(
        default=None,
        metadata={
            "name": "EndTimePrecision",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
