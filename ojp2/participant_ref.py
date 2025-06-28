from dataclasses import dataclass

from ojp2.participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class ParticipantRef(ParticipantRefStructure):
    """
    Reference to a Participant ([equivalent of PARTICIPANT in SIRI] IT system that
    is participating in a communication with other participant(s))
    """

    class Meta:
        namespace = "http://www.vdv.de/ojp"
