from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ojp.service_request_context_structure import ServiceRequestContextStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ContextualisedRequestStructure:
    """
    Type for General SIRI Request.

    :ivar service_request_context: General request properties -
        typically configured rather than repeated on request.
    :ivar request_timestamp:
    :ivar account_id: Account Identifier. May be used to attribute
        requests to a particular application provider and authentication
        key. The account  may be common to all users of an application,
        or to an individual user. Note that to identify an individual
        user the  RequestorRef can be used with an anonymised token.  .
        +SIRI v2.0
    :ivar account_key: Authentication key for request. May be used to
        authenticate requests from a particular account. +SIRI v2.0
    :ivar address: Address to which response is to be sent. This may
        also be determined from RequestorRef and preconfigured data.
    :ivar requestor_ref:
    :ivar message_identifier: Arbitrary unique identifier that can be
        used to reference this message in subsequent interactions.
    :ivar delegator_address: Address of original Consumer, i.e.
        requesting system to which delegating response is to be
        returned. +SIRI 2.0
    :ivar delegator_ref: Identifier of delegating system that originated
        message. +SIRI 2.0
    """
    service_request_context: Optional[ServiceRequestContextStructure] = field(
        default=None,
        metadata={
            "name": "ServiceRequestContext",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    request_timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RequestTimestamp",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    account_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountId",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    account_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountKey",
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
    requestor_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
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
