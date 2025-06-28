from dataclasses import dataclass, field

from ojp2.situation_full_ref_2 import SituationFullRef2

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class SituationRefList:
    """
    List of references to SITUATIONs.
    """

    situation_full_ref: list[SituationFullRef2] = field(
        default_factory=list,
        metadata={
            "name": "SituationFullRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
