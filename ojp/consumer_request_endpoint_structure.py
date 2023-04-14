from dataclasses import dataclass, field
from typing import Optional
from ojp.authenticated_request_structure import AuthenticatedRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ConsumerRequestEndpointStructure(AuthenticatedRequestStructure):
    """Type for Unique reference to this request, created by Consumer.

    May be used to reference the request in subsequent interactions.
    Used by WSDL.

    :ivar address: Address to which response is to be sent. This may
        also be determined from RequestorRef and preconfigured data.
    :ivar consumer_ref: Unique identifier of Consumer - a Participant
        reference.
    :ivar message_identifier: Arbitrary unique reference to this
        message. Some systems may use just timestamp for this.
    :ivar delegator_address: Address of original Consumer, i.e.
        requesting system to which delegating response is to be
        returned. +SIRI 2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    """
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    consumer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConsumerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
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
