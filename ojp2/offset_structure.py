from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class OffsetStructure:
    """
    Type for information about the LINEs affected by a SITUATION.

    :ivar distance_from_start: Distance in metres from start of link at
        which SITUATION is to be shown. I f absent use start of link.
    :ivar distance_from_end: Distance in metres from end of link at
        which SITUATION is to be shown. I f absent use end of link.
    """

    distance_from_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistanceFromStart",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distance_from_end: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistanceFromEnd",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
