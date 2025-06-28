from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DistributorVisitNumber:
    """
    Sequence of visit to Distributor stop within Distributor JOURNEY PATTERN.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
