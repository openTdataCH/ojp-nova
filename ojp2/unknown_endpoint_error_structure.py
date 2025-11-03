from dataclasses import dataclass, field
from typing import Optional

from ojp2.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownEndpointErrorStructure(ErrorCodeStructure):
    """Type for Error: Unknown Endpoint (since SIRI 2.0)

    :ivar endpoint: Endpoint that is noit known. + SIRI v2.0
    """

    endpoint: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
