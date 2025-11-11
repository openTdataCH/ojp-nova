from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class VisitNumber:
    """Sequence of visit to SCHEDULED STOP POINT.within VEHICLE JOURNEY.

    Increases monotonically, but not necessarily sequentially.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
