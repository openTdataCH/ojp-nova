from dataclasses import dataclass, field
from typing import Optional

from ojp2.encumbrance_enumeration import EncumbranceEnumeration
from ojp2.medical_need_enumeration import MedicalNeedEnumeration
from ojp2.mobility_enumeration import MobilityEnumeration
from ojp2.pyschosensory_need_enumeration import PyschosensoryNeedEnumeration

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class UserNeedStructure:
    """
    Type for of a specific need.

    :ivar mobility_need: Passenger mobility USER NEED for which
        SUITABILITY is specified.
    :ivar psychosensory_need: Passenger mobility USER NEED for which
        SUITABILITY is specified.
    :ivar medical_need: Passenger medical USER NEED for which
        SUITABILITY is specified.
    :ivar encumbrance_need: Passenger enceumbrance USER NEED for which
        SUITABILITY is specified.
    :ivar excluded: Whether USER NEED is included or excluded. Default
        is 'included'.
    :ivar need_ranking: Relative ranking of USER NEED on a sclae 1-5
    :ivar extensions: Extensions to USETR NEED.
    """

    mobility_need: Optional[MobilityEnumeration] = field(
        default=None,
        metadata={
            "name": "MobilityNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    psychosensory_need: Optional[PyschosensoryNeedEnumeration] = field(
        default=None,
        metadata={
            "name": "PsychosensoryNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    medical_need: Optional[MedicalNeedEnumeration] = field(
        default=None,
        metadata={
            "name": "MedicalNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    encumbrance_need: Optional[EncumbranceEnumeration] = field(
        default=None,
        metadata={
            "name": "EncumbranceNeed",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    excluded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Excluded",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    need_ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "NeedRanking",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    extensions: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
