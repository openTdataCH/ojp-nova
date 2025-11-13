from dataclasses import dataclass, field

from ojp2.communications_transport_method_enumeration import (
    CommunicationsTransportMethodEnumeration,
)
from ojp2.compression_method_enumeration import CompressionMethodEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class TransportDescriptionStructure:
    """
    Type for implementation structure.

    :ivar communications_transport_method: Communications Transport
        method used to exchange messages. Default is 'httpPost'.
    :ivar compression_method: Compression method used to compress
        messages for transmission. Default is 'none'.
    """

    communications_transport_method: CommunicationsTransportMethodEnumeration = field(
        default=CommunicationsTransportMethodEnumeration.HTTP_POST,
        metadata={
            "name": "CommunicationsTransportMethod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    compression_method: CompressionMethodEnumeration = field(
        default=CompressionMethodEnumeration.NONE,
        metadata={
            "name": "CompressionMethod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
