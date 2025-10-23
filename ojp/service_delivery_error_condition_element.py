from dataclasses import dataclass
from ojp.service_delivery_error_condition_structure import ServiceDeliveryErrorConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceDeliveryErrorConditionElement(ServiceDeliveryErrorConditionStructure):
    """
    Element fror an erroc condition for use in WSDL.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
