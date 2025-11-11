from dataclasses import dataclass, field
from typing import Optional

from ojp2.extensions_2 import Extensions2
from ojp2.request_structure import RequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CheckStatusRequestStructure(RequestStructure):
    """
    Type for check status request.

    :ivar extensions:
    :ivar version: Version number of request.
    """

    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
