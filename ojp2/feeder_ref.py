from dataclasses import dataclass

from ojp2.connecting_journey_ref_structure import ConnectingJourneyRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class FeederRef(ConnectingJourneyRefStructure):
    """Reference to a feeder VEHICLE JOURNEY.

    (since SIRI 2.0)
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
