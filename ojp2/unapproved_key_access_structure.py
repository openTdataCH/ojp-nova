from dataclasses import dataclass, field
from typing import Optional

from ojp2.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnapprovedKeyAccessStructure(ErrorCodeStructure):
    """Type for Error: UnapprovedKey (since SIRI 2.0)

    :ivar key: User key.
    """

    key: Optional[str] = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
