from dataclasses import dataclass

from ojp2.abstract_service_request_structure import (
    AbstractServiceRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractFunctionalServiceRequestStructure(
    AbstractServiceRequestStructure
):
    """
    Abstract Service Request for SIRI Service request.
    """
