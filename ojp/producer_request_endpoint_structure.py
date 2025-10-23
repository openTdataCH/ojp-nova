from dataclasses import dataclass, field
from typing import Optional
from ojp.authenticated_request_structure import AuthenticatedRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ProducerRequestEndpointStructure(AuthenticatedRequestStructure):
    """Type for Unique reference to request to the producer.

    May be used to reference request in subsequent interactions. Used
    for WSDL.

    :ivar address: Address to which response is to be sent. This may
        also be determined from ProducerRef and preconfigured data.
    :ivar producer_ref: Unique identifier of Producer - Participant
        reference.
    :ivar message_identifier: Arbitrary unique reference to this
        message. Some systems may use just timestamp for this. Where
        there are multiple SubscriptionFilters, this can be used to
        distinguish between different notifications for different
        filters.
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
    producer_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProducerRef",
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
