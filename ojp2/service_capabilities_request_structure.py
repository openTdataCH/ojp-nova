from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_service_request_structure import (
    AbstractServiceRequestStructure,
)
from ojp2.extensions_2 import Extensions2

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceCapabilitiesRequestStructure(AbstractServiceRequestStructure):
    """
    Type for ServcieCapabilities request.

    :ivar participant_permissions: Whether to include the requestors
        permissions in the response. Only applies if Access control
        capability supported. Default is 'false'.
    :ivar extensions:
    :ivar version: Version number of request. Fixed.
    """

    participant_permissions: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ParticipantPermissions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
