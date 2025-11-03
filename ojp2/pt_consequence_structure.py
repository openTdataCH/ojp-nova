from dataclasses import dataclass, field
from typing import Optional

from ojp2.affects_scope_structure import AffectsScopeStructure
from ojp2.blocking_structure import BlockingStructure
from ojp2.boarding_structure import BoardingStructure
from ojp2.casualties_structure import CasualtiesStructure
from ojp2.condition import Condition
from ojp2.delays_structure import DelaysStructure
from ojp2.easements_structure import EasementsStructure
from ojp2.extensions_2 import Extensions2
from ojp2.half_open_timestamp_output_range_structure import (
    HalfOpenTimestampOutputRangeStructure,
)
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.pt_advice_structure import PtAdviceStructure
from ojp2.severity_enumeration import SeverityEnumeration
from ojp2.suitability_structure import SuitabilityStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PtConsequenceStructure:
    """
    Type for disruption.

    :ivar period: Period of effect of disruption, if different from that
        of SITUATION.
    :ivar condition: Structured classification(s) of effect on service,
        from which a standardized message can be generated.
    :ivar condition_name: Textual classification of effect on service,
        from which a standardized message can be generated. Not normally
        needed, except when Condition is absent.
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

    period: list[HalfOpenTimestampOutputRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    condition: list[Condition] = field(
        default_factory=list,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    condition_name: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConditionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    severity: Optional[SeverityEnumeration] = field(
        default=None,
        metadata={
            "name": "Severity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affects: Optional[AffectsScopeStructure] = field(
        default=None,
        metadata={
            "name": "Affects",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    suitabilities: Optional["PtConsequenceStructure.Suitabilities"] = field(
        default=None,
        metadata={
            "name": "Suitabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advice: Optional[PtAdviceStructure] = field(
        default=None,
        metadata={
            "name": "Advice",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    blocking: Optional[BlockingStructure] = field(
        default=None,
        metadata={
            "name": "Blocking",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    boarding: Optional[BoardingStructure] = field(
        default=None,
        metadata={
            "name": "Boarding",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    delays: Optional[DelaysStructure] = field(
        default=None,
        metadata={
            "name": "Delays",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    casualties: Optional[CasualtiesStructure] = field(
        default=None,
        metadata={
            "name": "Casualties",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    easements: list[EasementsStructure] = field(
        default_factory=list,
        metadata={
            "name": "Easements",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class Suitabilities:
        """
        :ivar suitability: Effect on a passenger need.
        """

        suitability: list[SuitabilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
