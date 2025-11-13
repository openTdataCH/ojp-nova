from dataclasses import dataclass

from ojp2.participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RequestorRef(ParticipantRefStructure):
    """Reference to a requestor - Participant Code."""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
