from dataclasses import dataclass
from ojp.flexible_area_structure import FlexibleAreaStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AimedFlexibleArea(FlexibleAreaStructure):
    """Area that encompasses the scheduled flexible stop locations according to
    the planned timetable.

    (since SIRI 2.1)
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
