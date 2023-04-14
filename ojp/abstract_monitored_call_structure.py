from dataclasses import dataclass, field
from typing import List, Optional
from ojp.stop_point_name import StopPointName

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractMonitoredCallStructure:
    """
    Type for Abstract CALL at stop.

    :ivar stop_point_ref:
    :ivar visit_number:
    :ivar order:
    :ivar stop_point_name: Name of SCHEDULED STOP POINT.  (Unbounded
        since SIRI 2.0)
    """
    stop_point_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    visit_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    stop_point_name: List[StopPointName] = field(
        default_factory=list,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
