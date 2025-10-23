from dataclasses import dataclass
from ojp.abstract_response_context_structure import AbstractResponseContextStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripInfoResponseContextStructure(AbstractResponseContextStructure):
    """
    Context for a TripInfo response.
    """
