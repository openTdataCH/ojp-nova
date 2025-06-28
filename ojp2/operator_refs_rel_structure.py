from dataclasses import dataclass, field

from ojp2.operator_ref_structure import OperatorRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OperatorRefsRelStructure:
    class Meta:
        name = "OperatorRefs_RelStructure"

    operator_ref: list[OperatorRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "min_occurs": 1,
        },
    )
