from dataclasses import dataclass

from ojp2.direction_structure import DirectionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class Direction(DirectionStructure):
    """
    Description of a DIRECTION.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
