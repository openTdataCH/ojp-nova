from dataclasses import dataclass, field
from ojp.interchange_status_enumeration import InterchangeStatusEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class InterchangeStatusType:
    """
    Status of a SERVICE JOURNEY INTERCHANGE Status TPEG cross reference pti31.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: InterchangeStatusEnumeration = field(
        default=InterchangeStatusEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
