from dataclasses import dataclass

from ojp2.operator_ref_structure import OperatorRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DepartureOperatorRefs(OperatorRefStructure):
    """OPERATORs of service for departure and onwards.

    May change from that for arrival. (since SIRI 2.0).
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
