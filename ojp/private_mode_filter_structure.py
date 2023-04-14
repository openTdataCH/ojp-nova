from dataclasses import dataclass, field
from typing import List, Optional
from ojp.private_modes_enumeration import PrivateModesEnumeration

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class PrivateModeFilterStructure:
    """
    List of private mobility offers to include or exclude.

    :ivar exclude: Whether modes in list are to include or exclude from
        search. Default is exclude.
    :ivar private_mode: List of private mobility offers to
        include/exclude.
    """
    exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exclude",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    private_mode: List[PrivateModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PrivateMode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
