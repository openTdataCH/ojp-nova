from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AimedArrivalTimeOfFeeder:
    """Planned time at which feeder VEHICLE is scheduled to arrive.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
