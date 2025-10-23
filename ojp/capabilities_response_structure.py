from dataclasses import dataclass
from ojp.producer_response_structure import ProducerResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilitiesResponseStructure(ProducerResponseStructure):
    """
    Type for the capabilities of an implementation.
    """
