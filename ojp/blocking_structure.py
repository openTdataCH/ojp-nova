from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class BlockingStructure:
    """
    Type for blocking.

    :ivar journey_planner: Whether information about parts of the
        network identified by Affects should be blocked from computation
        made by a Journey Planner that has a real-tiem feed of the
        SITUATIONs. Default is 'false'; do not suppress.
    :ivar real_time: Whether information about parts of the network
        identified by Affects should be blocked from real-time
        departureinfo systems. Default is 'false'; do not suppress.
    """
    journey_planner: Optional[bool] = field(
        default=None,
        metadata={
            "name": "JourneyPlanner",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    real_time: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RealTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
