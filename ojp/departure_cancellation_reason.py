from dataclasses import dataclass
from ojp.natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DepartureCancellationReason(NaturalLanguageStringStructure):
    """Text annotation to be used in cases where DepartureStatus is set to
    'cancelled'.

    (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
