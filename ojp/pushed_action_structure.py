from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration
from ojp.parameterised_action_structure import ParameterisedActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PushedActionStructure(ParameterisedActionStructure):
    """
    Type for publication action.

    :ivar before_notices: Whether reminders should be sent.
    :ivar clear_notice: Whether a clearing notice should be displayed.
    """
    before_notices: Optional["PushedActionStructure.BeforeNotices"] = field(
        default=None,
        metadata={
            "name": "BeforeNotices",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    clear_notice: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ClearNotice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass
    class BeforeNotices:
        """
        :ivar interval: Intervals before validity start date to send
            reminders.
        """
        interval: List[XmlDuration] = field(
            default_factory=list,
            metadata={
                "name": "Interval",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            }
        )
