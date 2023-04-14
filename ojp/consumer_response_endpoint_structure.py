from dataclasses import dataclass, field
from typing import Optional
from ojp.response_structure import ResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ConsumerResponseEndpointStructure(ResponseStructure):
    """Type for Unique reference to this response created by Consumer.

    May be used to reference the request in subsequent interactions.
    Used by WSDL.

    :ivar consumer_ref: Unique identifier of Consumer - a Participant
        reference.
    :ivar request_message_ref: Reference to an arbitrary unique
        idenitifer associated with the request which gave rise to this
        response.
    :ivar delegator_address: Address of original Consumer, i.e.
        requesting system to which delegating response is to be
        returned. +SIRI 2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    """
    consumer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsumerRef",
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
    delegator_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    delegator_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "DelegatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
