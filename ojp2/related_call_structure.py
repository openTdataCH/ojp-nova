from dataclasses import dataclass, field
from typing import Optional

from ojp2.abstract_call_structure import AbstractCallStructure
from ojp2.aimed_arrival_time import AimedArrivalTime
from ojp2.aimed_departure_time import AimedDepartureTime

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RelatedCallStructure(AbstractCallStructure):
    """The JOURNEY RELATION refers to this CALL.

    (since SIRI 2.1)
    """

    aimed_departure_time: Optional[AimedDepartureTime] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_arrival_time: Optional[AimedArrivalTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
