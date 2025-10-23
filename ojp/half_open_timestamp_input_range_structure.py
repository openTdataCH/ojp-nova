from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ojp.end_time_precision_enumeration import EndTimePrecisionEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class HalfOpenTimestampInputRangeStructure:
    """Type for a range of date times.

    Start time must be specified, end time is optional.

    :ivar start_time: The (inclusive) start time stamp.
    :ivar end_time: The (inclusive) end time stamp.
    :ivar end_time_precision: Precision with which to interpret the
        inclusive end time. Default is to the second. (Siri 2.0++)
    """
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
