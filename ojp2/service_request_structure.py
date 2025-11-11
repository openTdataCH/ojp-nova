from dataclasses import dataclass

from ojp2.contextualised_request_structure import (
    ContextualisedRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceRequestStructure(ContextualisedRequestStructure):
    """
    SIRI Service Request.
    """
