from dataclasses import dataclass

from ojp2.authenticated_request_structure import AuthenticatedRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AuthenticatedRequest(AuthenticatedRequestStructure):
    """
    Subsititutable type for an authenticated request Authenticated.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
