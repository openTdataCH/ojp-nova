from dataclasses import dataclass, field
from typing import Optional

from ojp2.dated_journey_structure import DatedJourneyStructure
from ojp2.emission_co2_structure import EmissionCo2Structure
from ojp2.international_text_structure import InternationalTextStructure
from ojp2.leg_alight_structure import LegAlightStructure
from ojp2.leg_attribute_structure import LegAttributeStructure
from ojp2.leg_board_structure import LegBoardStructure
from ojp2.leg_intermediate_structure import LegIntermediateStructure
from ojp2.leg_track_structure import LegTrackStructure
from ojp2.operating_days_structure import OperatingDaysStructure
from ojp2.parallel_service_structure import ParallelServiceStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class TimedLegStructure:
    """Corresponds to a RIDE or PT RIDE LEG in TM 6.2 with the attribute Timed
    (with related information).

    Passenger LEG with timetabled schedule.

    :ivar leg_board: Stop/Station where boarding is done
    :ivar leg_intermediate: Information about the intermediate passed
        stop points.
    :ivar leg_alight: Stop/Station to alight
    :ivar service: Service that is used for this leg.
    :ivar leg_attribute: Attributes that are not valid on the whole
        service, but only on parts of the journey leg.
    :ivar operating_days: Bit string definition of operating days.
    :ivar operating_days_description: Textual description of the
        operation days, e.g., "Monday to Friday" or "not on holidays".
    :ivar leg_track: Geographic embedding of this leg.
    :ivar parallel_service: Services running combined with at least
        parts of this journey, e.g., wing trains. The contained stop
        sequence interval refers to the original journey.
    :ivar emission_co2: Estimation of CO2 emissions.
    :ivar extension:
    """

    leg_board: Optional[LegBoardStructure] = field(
        default=None,
        metadata={
            "name": "LegBoard",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
        },
    )
    leg_intermediate: list[LegIntermediateStructure] = field(
        default_factory=list,
        metadata={
            "name": "LegIntermediate",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    leg_alight: Optional[LegAlightStructure] = field(
        default=None,
        metadata={
            "name": "LegAlight",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
            "required": True,
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
    leg_attribute: list[LegAttributeStructure] = field(
        default_factory=list,
        metadata={
            "name": "LegAttribute",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
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
    leg_track: Optional[LegTrackStructure] = field(
        default=None,
        metadata={
            "name": "LegTrack",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
    parallel_service: list[ParallelServiceStructure] = field(
        default_factory=list,
        metadata={
            "name": "ParallelService",
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
    extension: Optional[object] = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "http://www.vdv.de/ojp",
        },
    )
