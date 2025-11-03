from dataclasses import dataclass, field
from typing import Optional

from ojp2.user_need_structure import UserNeedStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class PassengerAccessibilityNeedsStructure:
    """Type for accessibility needs.

    Records the requirementrs of a passenger that may affect choice of
    facilities.

    :ivar user_need: Specific pyschosensory need that may constrain
        choice of services and facilities.
    :ivar accompanied_by_carer: Whether the passenger is accompanied by
        a carer or assistant.
    """

    user_need: list[UserNeedStructure] = field(
        default_factory=list,
        metadata={
            "name": "UserNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    accompanied_by_carer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccompaniedByCarer",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
