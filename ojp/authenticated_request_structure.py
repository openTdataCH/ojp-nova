from dataclasses import dataclass, field
from typing import Optional
from ojp.abstract_request_structure import AbstractRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AuthenticatedRequestStructure(AbstractRequestStructure):
    """
    Type for Authticated SIRI Request.

    :ivar account_id: Account Identifier. May be used to attribute
        requests to a particular application provider and authentication
        key. The account  may be common to all users of an application,
        or to an individual user. Note that to identify an individual
        user the  RequestorRef can be used with an anonymised token.  .
        +SIRI v2.0
    :ivar account_key: Authentication key for request. May be used to
        authenticate requests from a particular account. +SIRI v2.0
    """
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
