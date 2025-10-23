from dataclasses import dataclass, field
from typing import List, Optional
from ojp.affects_scope_structure import AffectsScopeStructure
from ojp.blocking_structure import BlockingStructure
from ojp.boarding_structure import BoardingStructure
from ojp.casualties_structure import CasualtiesStructure
from ojp.delays_structure import DelaysStructure
from ojp.easements_structure import EasementsStructure
from ojp.extensions_1 import Extensions1
from ojp.half_open_timestamp_output_range_structure import HalfOpenTimestampOutputRangeStructure
from ojp.pt_advice_structure import PtAdviceStructure
from ojp.service_condition_enumeration import ServiceConditionEnumeration
from ojp.severity_enumeration import SeverityEnumeration
from ojp.suitability_structure import SuitabilityStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PtConsequenceStructure:
    """
    Type for disruption.

    :ivar period: Period of effect of disruption, if different from that
        of SITUATION.
    :ivar condition:
    :ivar severity: Severity of disruption if different from that of
        SITUATION. TPEG pti26
    :ivar affects: Parts of transport network affected by disruption if
        different from that of SITUATION.
    :ivar suitabilities: Effect on different passenger needs.
    :ivar advice: Advice to passengers.
    :ivar blocking: How Disruption should be handled in Info systems.
    :ivar boarding: Change to normal boarding activity allowed at stop.
    :ivar delays:
    :ivar casualties: Information on casualties.
    :ivar easements: Description of fare exceptions allowed because of
        disruption.
    :ivar extensions:
    """
    period: Optional[HalfOpenTimestampOutputRangeStructure] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    condition: List[ServiceConditionEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    severity: Optional[SeverityEnumeration] = field(
        default=None,
        metadata={
            "name": "Severity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    affects: Optional[AffectsScopeStructure] = field(
        default=None,
        metadata={
            "name": "Affects",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    suitabilities: Optional["PtConsequenceStructure.Suitabilities"] = field(
        default=None,
        metadata={
            "name": "Suitabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    advice: Optional[PtAdviceStructure] = field(
        default=None,
        metadata={
            "name": "Advice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    blocking: Optional[BlockingStructure] = field(
        default=None,
        metadata={
            "name": "Blocking",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    boarding: Optional[BoardingStructure] = field(
        default=None,
        metadata={
            "name": "Boarding",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    delays: Optional[DelaysStructure] = field(
        default=None,
        metadata={
            "name": "Delays",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    casualties: Optional[CasualtiesStructure] = field(
        default=None,
        metadata={
            "name": "Casualties",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    easements: List[EasementsStructure] = field(
        default_factory=list,
        metadata={
            "name": "Easements",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass
    class Suitabilities:
        """
        :ivar suitability: Effect on a passenger need.
        """
        suitability: List[SuitabilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            }
        )
