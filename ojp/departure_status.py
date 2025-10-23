from dataclasses import dataclass, field
from typing import Optional
from ojp.call_status_enumeration import CallStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DepartureStatus:
    """Classification of the timeliness of the departure part of the CALL,
    according to a fixed list of values.

    This may reflect a presentation policy, for example CALLs less than
    one minute behind target time are still classified as on-time.
    Applications may use this to guide their own presentation of times.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[CallStatusEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
