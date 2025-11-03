from dataclasses import dataclass

from ojp2.stop_point_ref_structure import StopPointRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FeederArrivalStopRef(StopPointRefStructure):
    """SCHEDULED STOP POINT at which feeder journey arrives.

    (since SIRI 2.0)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
