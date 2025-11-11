from dataclasses import dataclass

from ojp2.journey_pattern_ref_structure import JourneyPatternRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class JourneyPatternRef(JourneyPatternRefStructure):
    """
    Reference to a JOURNEY PATTERN.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
