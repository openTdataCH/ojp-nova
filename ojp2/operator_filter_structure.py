from dataclasses import dataclass, field
from typing import Optional

from ojp2.operator_ref_structure import OperatorRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OperatorFilterStructure:
    """
    Filter for in/exclusion of transport operators.

    :ivar exclude: Whether operators in list are to include or exclude
        from search. Default is exclude.
    :ivar operator_ref: Reference to transport operator
    """

    exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Exclude",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    operator_ref: list[OperatorRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
