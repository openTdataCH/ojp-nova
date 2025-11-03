from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.end_time_status_enumeration import EndTimeStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class HalfOpenTimestampOutputRangeStructure:
    """Type for a range of date times.

    Start time must be specified, end time is optional.

    :ivar start_time: The (inclusive) start time stamp.
    :ivar end_time: The (inclusive) end time stamp. If omitted, the
        range end is open-ended, that is, it should be interpreted as
        defined by end time status.
    :ivar end_time_status: If end time not provided, whethhr to
        interpret range as long, term, short term or unknown length of
        situation. Default is unknown. (Siri 2.0++)
    """

    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    end_time_status: Optional[EndTimeStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "EndTimeStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
