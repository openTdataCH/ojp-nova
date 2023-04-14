from dataclasses import dataclass
from ojp.formation_assignment_structure import FormationAssignmentStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DepartureFormationAssignment(FormationAssignmentStructure):
    """Assignment of a TRAIN formation to a physical QUAY (platform or sectors
    thereof).

    (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
