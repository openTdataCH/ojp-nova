from dataclasses import dataclass

from ojp2.interchange_ref_structure import InterchangeRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class InterchangeRef(InterchangeRefStructure):
    """
    Reference to a SERVICE JOURNEY  INTERCHANGE.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
