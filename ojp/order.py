from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class Order:
    """
    For implementations for which the overall Order is not used for VisitNumber,
    (i.e. if VisitNumberIsOrder is false) then can be used to associate the stop
    Order as well if useful.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
