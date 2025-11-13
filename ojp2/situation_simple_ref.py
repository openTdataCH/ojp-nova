from dataclasses import dataclass

from ojp2.situation_simple_ref_structure import SituationSimpleRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SituationSimpleRef(SituationSimpleRefStructure):
    """
    Reference to a SITUATION associated with the element.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
