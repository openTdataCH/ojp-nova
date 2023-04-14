from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class HalfOpenTimeRangeStructure1:
    """Type for a range of times.

    Start time must be specified, end time is optional.

    :ivar start_time: The (inclusive) start time.
    :ivar end_time: The (inclusive) end time. If omitted, the range end
        is open-ended, that is, it should be interpreted as "forever".
    """
    class Meta:
        name = "HalfOpenTimeRangeStructure"

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
        }
    )
