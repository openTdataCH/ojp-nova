from dataclasses import dataclass

from ojp2.flexible_area_ref_structure import FlexibleAreaRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AimedFlexibleAreaRef(FlexibleAreaRefStructure):
    """Reference to the scheduled location or flexible area.

    (since SIRI 2.1)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
