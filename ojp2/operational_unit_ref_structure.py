from dataclasses import dataclass

from ojp2.operator_ref_structure import OperatorRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class OperationalUnitRefStructure(OperatorRefStructure):
    """
    Type for reference to an Operatorational Unit Code.
    """
