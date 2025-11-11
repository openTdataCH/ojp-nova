from dataclasses import dataclass

from ojp2.formation_assignment_structure import FormationAssignmentStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ArrivalFormationAssignment(FormationAssignmentStructure):
    """Assignment of a TRAIN formation to a physical QUAY (platform or sectors
    thereof).

    If not given, assume same as for departure. (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
