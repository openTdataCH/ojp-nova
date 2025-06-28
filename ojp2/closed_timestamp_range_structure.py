from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ClosedTimestampRangeStructure:
    """Type for a range of date and times.

    Both start and end time are required.

    :ivar start_time: The (inclusive) start date and time.
    :ivar end_time: The (inclusive) end date and time.
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
            "required": True,
        },
    )
