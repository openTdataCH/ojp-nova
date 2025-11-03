from dataclasses import dataclass, field
from typing import Optional

from ojp2.call_at_near_stop_structure import CallAtNearStopStructure
from ojp2.dated_journey_structure import DatedJourneyStructure
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.operating_days_structure import OperatingDaysStructure
from ojp2.situation_ref_list import SituationRefList

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class StopEventStructure:
    """
    Stop event structure.

    :ivar previous_call: Calls at stops that happen before this stop
        event (service pattern of this vehicle journey before this stop
        event).
    :ivar this_call: The call of this vehicle journey at this stop.
    :ivar onward_call: Calls at stops that happen after this stop event
        (rest of the service pattern of the vehicle journey).
    :ivar service: Service that calls at this stop.
    :ivar operating_days: Bit string definition of operating days.
    :ivar operating_days_description: Textual description of the
        operation days, e.g., "Monday to Friday" or "not on holidays".
    :ivar situation_full_refs: For SITUATIONs that affect the whole
        StopEvent. Otherwise, references for SITUATIONs can be added at
        the different CALL elements
    :ivar extension:
    """

    previous_call: list[CallAtNearStopStructure] = field(
        default_factory=list,
        metadata={
            "name": "PreviousCall",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    this_call: Optional[CallAtNearStopStructure] = field(
        default=None,
        metadata={
            "name": "ThisCall",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    onward_call: list[CallAtNearStopStructure] = field(
        default_factory=list,
        metadata={
            "name": "OnwardCall",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    service: Optional[DatedJourneyStructure] = field(
        default=None,
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    operating_days: Optional[OperatingDaysStructure] = field(
        default=None,
        metadata={
            "name": "OperatingDays",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    operating_days_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "OperatingDaysDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    situation_full_refs: Optional[SituationRefList] = field(
        default=None,
        metadata={
            "name": "SituationFullRefs",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
