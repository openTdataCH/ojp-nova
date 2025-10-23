from dataclasses import dataclass
from ojp.unknown_participant_error_structure import UnknownParticipantErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownParticipantError(UnknownParticipantErrorStructure):
    """Error: Recipient for a message to be distributed is unknown. +SIRI v2.0"""
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
