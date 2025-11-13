from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from ojp2.continuous_leg_structure import ContinuousLegStructure
from ojp2.emission_co2_structure import EmissionCo2Structure
from ojp2.participant_ref_structure import ParticipantRefStructure
from ojp2.timed_leg_structure import TimedLegStructure
from ojp2.transfer_leg_structure import TransferLegStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class LegStructure:
    """A single stage of a TRIP that is made without change of MODE or service
    (e.g., between each interchange).

    Implements LEG from TM 6.2.

    :ivar id: Id of this leg. Unique within trip result.
    :ivar participant_ref: [equivalent of PARTICIPANT in SIRI] IT system
        that is participating in a communication with other
        participant(s)
    :ivar duration: The duration of the LEG (e.g., from Transmodel PT
        RIDE LEG.Duration).
    :ivar timed_leg: Corresponds to a RIDE or PT RIDE LEG in TM 6.2 with
        the attribute Timed (with related information). Passenger LEG
        with timetabled schedule.
    :ivar transfer_leg: TRANSFER LEG or CONNECTION LEG according to TM
        6.2. Description of a LEG which links other LEGs where a
        TRANSFER or CONNECTION between different LOCATIONs is required.
    :ivar continuous_leg: A specialised type of RIDE LEG in with
        Timed=false, a PERSONAL LEG or an ACCESS LEG TM 6 and NeTEx. LEG
        of a TRIP that is not bound to a timetable.
    :ivar emission_co2: Estimation of CO2 emissions.
    :ivar changed: TRUE if leg got changed by TripChange-Request.
    """

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    participant_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    timed_leg: Optional[TimedLegStructure] = field(
        default=None,
        metadata={
            "name": "TimedLeg",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    transfer_leg: Optional[TransferLegStructure] = field(
        default=None,
        metadata={
            "name": "TransferLeg",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    continuous_leg: Optional[ContinuousLegStructure] = field(
        default=None,
        metadata={
            "name": "ContinuousLeg",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    emission_co2: Optional[EmissionCo2Structure] = field(
        default=None,
        metadata={
            "name": "EmissionCO2",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    changed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Changed",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
