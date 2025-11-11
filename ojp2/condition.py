from dataclasses import dataclass, field
from typing import Optional

from ojp2.service_condition_enumeration import ServiceConditionEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class Condition:
    """Classification of effect on service.

    TPEG PTS043 ServiceStatus
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[ServiceConditionEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
