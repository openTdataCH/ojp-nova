from dataclasses import dataclass

from ojp2.abstract_service_request_structure import (
    AbstractServiceRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractServiceRequest(AbstractServiceRequestStructure):
    """
    Substitutable type for a SIRI Functional Service request.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
