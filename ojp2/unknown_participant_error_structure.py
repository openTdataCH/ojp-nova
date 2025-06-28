from dataclasses import dataclass, field
from typing import Optional

from ojp2.error_code_structure import ErrorCodeStructure
from ojp2.participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownParticipantErrorStructure(ErrorCodeStructure):
    """Type for Error: Unknown Participant. (since SIRI 2.0)

    :ivar participant_ref: Reference to  Participant who is unknown. +
        SIRI v2.0
    """

    participant_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
