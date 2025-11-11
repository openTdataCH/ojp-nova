from dataclasses import dataclass

from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ReasonForRemoval(NaturalLanguageStringStructure):
    """The data producer must provide a reason, e.g. type of error and description,
    in case he wants to silently remove (instead of cancel) a journey or an
    interchange from the plan.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
