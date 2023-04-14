from dataclasses import dataclass, field
from typing import Optional
from ojp.suitability_enumeration import SuitabilityEnumeration
from ojp.user_need_structure import UserNeedStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class SuitabilityStructure:
    """
    Type for of a specific SUITABILITY.

    :ivar suitable: Whether the Facility is suitable.
    :ivar user_need: USER NEED for which SUITABILITY is specified.
    """
    suitable: Optional[SuitabilityEnumeration] = field(
        default=None,
        metadata={
            "name": "Suitable",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
            "required": True,
        }
    )
    user_need: Optional[UserNeedStructure] = field(
        default=None,
        metadata={
            "name": "UserNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
            "required": True,
        }
    )
