from dataclasses import dataclass, field
from typing import Optional

from ojp2.alternative_modes_of_operation_enumeration import (
    AlternativeModesOfOperationEnumeration,
)
from ojp2.personal_modes_enumeration import PersonalModesEnumeration
from ojp2.personal_modes_of_operation_enumeration import (
    PersonalModesOfOperationEnumeration,
)

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ItModesStructure:
    """Combinations of MODE and MODE OF OPERATION that should be covered as
    monomodal trips (or for the ACCESS LEGs).

    If no MODE OF OPERATION is added usually "own" is assumed. But the
    trip planner may add other relevant results (e.g., sharing, if
    sensible trips are possible).

    :ivar personal_mode: Relevant PERSONAL MODE to be used for the
        monomodal trip.
    :ivar personal_mode_of_operation: List of personal mobility offers
        for this MODE.
    :ivar alternative_mode_of_operation: List of alternative mobility
        offers for this MODE.
    """

    personal_mode: Optional[PersonalModesEnumeration] = field(
        default=None,
        metadata={
            "name": "PersonalMode",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    personal_mode_of_operation: list[PersonalModesOfOperationEnumeration] = (
        field(
            default_factory=list,
            metadata={
                "name": "PersonalModeOfOperation",
                "type": "Element",
                "namespace": "http://www.vdv.de/ojp",
            },
        )
    )
    alternative_mode_of_operation: list[
        AlternativeModesOfOperationEnumeration
    ] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeModeOfOperation",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
