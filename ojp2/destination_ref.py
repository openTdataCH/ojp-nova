from dataclasses import dataclass

from ojp2.destination_ref_structure import DestinationRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DestinationRef(DestinationRefStructure):
    """
    Reference to the destination SCHEDULED STOP POINT of the journey.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
