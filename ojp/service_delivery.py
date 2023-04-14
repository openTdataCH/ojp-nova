from dataclasses import dataclass
from ojp.service_delivery_structure import ServiceDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceDelivery(ServiceDeliveryStructure):
    """Response from Producer to Consumer to deliver payload data.

    Either answers a direct ServiceRequest, or asynchronously satisfies
    a subscription. May be sent directly in one step, or fetched in
    response to a DataSupply Request.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
