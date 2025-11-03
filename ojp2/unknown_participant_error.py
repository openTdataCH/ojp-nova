from dataclasses import dataclass

from ojp2.unknown_participant_error_structure import (
    UnknownParticipantErrorStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownParticipantError(UnknownParticipantErrorStructure):
    """Error: Recipient for a message to be distributed is unknown. (since SIRI 2.0)"""

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
