from dataclasses import dataclass, field
from typing import Optional

from ojp2.call_status_enumeration import CallStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ArrivalStatus:
    """Classification of the timeliness of the visit according to a fixed list of
    values.

    If not specified, same as DepartureStatus.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[CallStatusEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
