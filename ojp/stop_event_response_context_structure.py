from dataclasses import dataclass
from ojp.abstract_response_context_structure import AbstractResponseContextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopEventResponseContextStructure(AbstractResponseContextStructure):
    """Stop event response context.

    May hold objects that are referenced several times.
    """
