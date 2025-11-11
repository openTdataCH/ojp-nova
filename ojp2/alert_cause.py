from dataclasses import dataclass, field
from typing import Optional

from ojp2.alert_cause_enumeration import AlertCauseEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AlertCause:
    """TPEG Pts38: AlertCause."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[AlertCauseEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
