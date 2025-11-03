from dataclasses import dataclass, field
from typing import Optional

from ojp2.request_timestamp import RequestTimestamp

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractRequestStructure:
    """
    Type for General SIRI Request.
    """

    request_timestamp: Optional[RequestTimestamp] = field(
        default=None,
        metadata={
            "name": "RequestTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
