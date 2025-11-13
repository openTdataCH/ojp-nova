from dataclasses import dataclass

from ojp2.abstract_functional_service_request_structure import (
    AbstractFunctionalServiceRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractFunctionalServiceRequest(
    AbstractFunctionalServiceRequestStructure
):
    """
    Subsititutable type for a SIRI Functional Service request.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
