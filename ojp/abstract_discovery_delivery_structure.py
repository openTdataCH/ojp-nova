from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from ojp.response_structure import ResponseStructure
from ojp.service_delivery_error_condition_structure import ServiceDeliveryErrorConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractDiscoveryDeliveryStructure(ResponseStructure):
    """
    Abstract supertype fro discovery responses.

    :ivar status:
    :ivar error_condition: Description of any error or warning
        condition.
    :ivar valid_until: End of data horizon of the data producer.
    :ivar shortest_possible_cycle: Minimum interval at which updates can
        be sent.
    """
    status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    error_condition: Optional[ServiceDeliveryErrorConditionStructure] = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    valid_until: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    shortest_possible_cycle: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ShortestPossibleCycle",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
