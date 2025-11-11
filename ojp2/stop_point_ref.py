from dataclasses import dataclass

from ojp2.stop_point_ref_structure import StopPointRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class StopPointRef(StopPointRefStructure):
    """Reference to a SCHEDULED STOP POINT.

    Reference to a STOP POINT.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
