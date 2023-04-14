from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ojp.abstract_call_structure import AbstractCallStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RelatedCallStructure(AbstractCallStructure):
    """The JOURNEY RELATION refers to this CALL.

    (since SIRI 2.1)
    """
    aimed_departure_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    aimed_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
