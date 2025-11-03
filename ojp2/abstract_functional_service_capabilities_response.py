from dataclasses import dataclass

from ojp2.abstract_service_capabilities_response_structure import (
    AbstractServiceCapabilitiesResponseStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractFunctionalServiceCapabilitiesResponse(
    AbstractServiceCapabilitiesResponseStructure
):
    """
    Subsititutable type for a SIRI Functional Service Capabiloitiesequest.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
