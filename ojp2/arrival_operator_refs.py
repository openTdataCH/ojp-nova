from dataclasses import dataclass

from ojp2.operator_ref_structure import OperatorRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ArrivalOperatorRefs(OperatorRefStructure):
    """OPERATORs of of service up until arrival.

    May change for departure. (since SIRI 2.0).
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
