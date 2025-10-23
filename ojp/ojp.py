from dataclasses import dataclass, field
from typing import Optional
from ojp.extensions_1 import Extensions1
from ojp.ojprequest import Ojprequest
from ojp.ojpresponse import Ojpresponse

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class Ojp:
    """
    Root element for OJP messages based on SIRI message exchange protocol.
    """
    class Meta:
        name = "OJP"
        namespace = "http://www.siri.org.uk/siri"

    ojprequest: Optional[Ojprequest] = field(
        default=None,
        metadata={
            "name": "OJPRequest",
            "type": "Element",
        }
    )
    ojpresponse: Optional[Ojpresponse] = field(
        default=None,
        metadata={
            "name": "OJPResponse",
            "type": "Element",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
        }
    )
    version: str = field(
        init=False,
        default="1.0",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
