from dataclasses import dataclass, field
from typing import Optional
from ojp.continuous_leg_structure import ContinuousLegStructure
from ojp.timed_leg_structure import TimedLegStructure
from ojp.transfer_leg_structure import TransferLegStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TripLegStructure:
    """
    a single stage of a TRIP that is made without change of MODE or service
    (ie: between each interchange)

    :ivar leg_id: Id of this trip leg. Unique within trip result.
    :ivar participant_ref: [equivalent of PARTICIPANT in SIRI] IT system
        that is participating in a communication with other
        participant(s)
    :ivar timed_leg:
    :ivar transfer_leg:
    :ivar continuous_leg:
    """
    leg_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegId",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    timed_leg: Optional[TimedLegStructure] = field(
        default=None,
        metadata={
            "name": "TimedLeg",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    transfer_leg: Optional[TransferLegStructure] = field(
        default=None,
        metadata={
            "name": "TransferLeg",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    continuous_leg: Optional[ContinuousLegStructure] = field(
        default=None,
        metadata={
            "name": "ContinuousLeg",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
