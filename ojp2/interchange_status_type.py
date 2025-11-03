from dataclasses import dataclass, field

from ojp2.interchange_status_enumeration import InterchangeStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class InterchangeStatusType:
    """Status of a SERVICE JOURNEY INTERCHANGE - TPEG Pti31 InterchangeStatus"""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: InterchangeStatusEnumeration = field(
        default=InterchangeStatusEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
