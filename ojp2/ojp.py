from dataclasses import dataclass, field
from typing import Optional

from ojp2.extensions_2 import Extensions2
from ojp2.ojprequest import Ojprequest
from ojp2.ojpresponse import Ojpresponse

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class Ojp:
    """
    Root element for OJP messages based on SIRI message exchange protocol.
    """

    class Meta:
        name = "OJP"
        namespace = "http://www.vdv.de/ojp"

    ojprequest: Optional[Ojprequest] = field(
        default=None,
        metadata={
            "name": "OJPRequest",
            "type": "Element",
        },
    )
    ojpresponse: Optional[Ojpresponse] = field(
        default=None,
        metadata={
            "name": "OJPResponse",
            "type": "Element",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    version: str = field(
        init=False,
        default="2.0",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
