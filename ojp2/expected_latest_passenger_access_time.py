from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ExpectedLatestPassengerAccessTime:
    """Latest expected time at which a PASSENGER should aim to arrive at the STOP
    PLACE containing the stop.

    This time may be earlier than the VEHICLE departure times and may
    include time for processes such as checkin, security, etc.(As
    specified by CHECK CONSTRAINT DELAYs in the underlying data). If
    absent assume to be the same as Earliest expected departure time.
    (since SIRI 2.0)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
