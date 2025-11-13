from dataclasses import dataclass

from ojp2.formation_condition_structure import FormationConditionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FormationCondition(FormationConditionStructure):
    """Information about a change of the formation (e.g. TRAIN composition) or
    changes of vehicles within the formation.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
