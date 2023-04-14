from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AimedHeadwayInterval:
    """
    For frequency based services, target interval between vehicles at stop.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
