from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FeederVisitNumber:
    """
    Sequence of visit to Feeder stop within Feeder JOURNEY PATTERN.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
