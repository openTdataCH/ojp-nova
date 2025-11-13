from dataclasses import dataclass, field
from typing import Optional

from ojp2.response_timestamp import ResponseTimestamp

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ResponseStructure:
    """
    General Type for General SIRI Response.
    """

    response_timestamp: Optional[ResponseTimestamp] = field(
        default=None,
        metadata={
            "name": "ResponseTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
