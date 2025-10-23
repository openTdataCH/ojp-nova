from dataclasses import dataclass, field
from typing import Optional
from nova.client_identifier import ClientIdentifier

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class Ping:
    class Meta:
        name = "ping"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    client_identifier: Optional[ClientIdentifier] = field(
        default=None,
        metadata={
            "name": "clientIdentifier",
            "type": "Element",
            "required": True,
        }
    )
