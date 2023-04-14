from dataclasses import dataclass, field
from typing import Optional
from ojp.response_structure import ResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ProducerResponseEndpointStructure(ResponseStructure):
    """Type for Unique reference to reponse from producer.

    May be used to reference request in subsequent interactions. Used
    for WSDL.

    :ivar producer_ref: Unique identifier of Producer - Participant
        reference.
    :ivar address: Endpoint Address to which acknowledgements to confirm
        delivery are to be sent.
    :ivar response_message_identifier: An arbitrary unique reference
        associated with the response which may be used to reference it.
    :ivar request_message_ref: Reference to an arbitrary unique
        identifier associated with the request which gave rise to this
        response.
    """
    producer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProducerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    response_message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResponseMessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    request_message_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
