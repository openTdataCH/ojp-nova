from dataclasses import dataclass, field
from typing import List, Optional
from ojp.dated_journey_structure import DatedJourneyStructure
from ojp.international_text_structure import InternationalTextStructure
from ojp.leg_alight_structure import LegAlightStructure
from ojp.leg_attribute_structure import LegAttributeStructure
from ojp.leg_board_structure import LegBoardStructure
from ojp.leg_intermediate_structure import LegIntermediateStructure
from ojp.leg_track_structure import LegTrackStructure
from ojp.operating_days_structure import OperatingDaysStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TimedLegStructure:
    """Passenger TRIP LEG with timetabled schedule.

    Corresponds to a RIDE.

    :ivar leg_board: Stop/Station where boarding is done
    :ivar leg_intermediates: information about the intermediate passed
        stop points.
    :ivar leg_alight: Stop/Station to alight
    :ivar service: Service that is used for this trip leg.
    :ivar leg_attribute: Attributes that are not valid on the whole
        service, but only on parts of the journey leg.
    :ivar operating_days: Bit string definition of operating days.
    :ivar operating_days_description: Textual description of the
        operation days, e.g. "monday to friday" or "not on holidays".
    :ivar leg_track: Geographic embedding of this leg.
    :ivar extension:
    """
    leg_board: Optional[LegBoardStructure] = field(
        default=None,
        metadata={
            "name": "LegBoard",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    leg_intermediates: List[LegIntermediateStructure] = field(
        default_factory=list,
        metadata={
            "name": "LegIntermediates",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    leg_alight: Optional[LegAlightStructure] = field(
        default=None,
        metadata={
            "name": "LegAlight",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    service: Optional[DatedJourneyStructure] = field(
        default=None,
        metadata={
            "name": "Service",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        }
    )
    leg_attribute: List[LegAttributeStructure] = field(
        default_factory=list,
        metadata={
            "name": "LegAttribute",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    operating_days: Optional[OperatingDaysStructure] = field(
        default=None,
        metadata={
            "name": "OperatingDays",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    operating_days_description: Optional[InternationalTextStructure] = field(
        default=None,
        metadata={
            "name": "OperatingDaysDescription",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    leg_track: Optional[LegTrackStructure] = field(
        default=None,
        metadata={
            "name": "LegTrack",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        }
    )
