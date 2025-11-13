from dataclasses import dataclass

from ojp2.abstract_service_delivery_structure import (
    AbstractServiceDeliveryStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractFunctionalServiceDelivery(AbstractServiceDeliveryStructure):
    """
    Subsititutable type for a SIRI Functional Service request.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
