from dataclasses import dataclass

from ojp2.situation_ref_structure import SituationRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SituationRef(SituationRefStructure):
    """
    Reference to a SITUATION associated with the element.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
