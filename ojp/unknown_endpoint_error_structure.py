from dataclasses import dataclass, field
from typing import Optional
from ojp.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownEndpointErrorStructure(ErrorCodeStructure):
    """
    Type for Error: Unknown Endpoint +SIRI v2.0.

    :ivar endpoint: Endpoint that is not known. + SIRI v2.0
    """
    endpoint: Optional[str] = field(
        default=None,
        metadata={
            "name": "Endpoint",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
