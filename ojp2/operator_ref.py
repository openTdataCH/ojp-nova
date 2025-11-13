from dataclasses import dataclass

from ojp2.operator_ref_structure import OperatorRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class OperatorRef(OperatorRefStructure):
    """
    Reference to an Operator ([TMv6] company  providing public transport services.)
    """

    class Meta:
        namespace = "http://www.vdv.de/ojp"
