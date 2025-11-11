from dataclasses import dataclass, field
from typing import Optional

from ojp2.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilityNotSupportedErrorStructure(ErrorCodeStructure):
    """Type for Error: Service does not support requested capability.

    :ivar capability_ref: Id of capabiliuty that is noit supported.
    """

    capability_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "CapabilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
