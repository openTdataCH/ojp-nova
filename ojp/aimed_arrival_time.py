from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AimedArrivalTime:
    """
    Target arrival time of VEHICLE at stop according to latest working timetable.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
