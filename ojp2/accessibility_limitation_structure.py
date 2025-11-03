from dataclasses import dataclass, field
from typing import Optional

from ojp2.audible_signals_available import AudibleSignalsAvailable
from ojp2.escalator_free_access import EscalatorFreeAccess
from ojp2.extensions_1 import Extensions1
from ojp2.lift_free_access import LiftFreeAccess
from ojp2.step_free_access import StepFreeAccess
from ojp2.validity_condition_structure import ValidityConditionStructure
from ojp2.visual_signs_available import VisualSignsAvailable
from ojp2.wheelchair_access import WheelchairAccess

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class AccessibilityLimitationStructure:
    """
    Type for limitation on navigation.

    :ivar limitation_id: Identifier of LIMITATION.
    :ivar validity_condition: Validity condition governing applicability
        of LIMITATION.
    :ivar wheelchair_access:
    :ivar step_free_access:
    :ivar escalator_free_access:
    :ivar lift_free_access:
    :ivar audible_signals_available: Whether a PLACE / SITE ELEMENT has
        Audible signals for the visually impaired. Default is 'false'.
    :ivar visual_signs_available: Whether a PLACE / SITE ELEMENT has
        Visual signals for the hearing impaired. Default is 'unknown'.
    :ivar extensions:
    """

    limitation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LimitationId",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    validity_condition: Optional[ValidityConditionStructure] = field(
        default=None,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    wheelchair_access: Optional[WheelchairAccess] = field(
        default=None,
        metadata={
            "name": "WheelchairAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
            "required": True,
        },
    )
    step_free_access: Optional[StepFreeAccess] = field(
        default=None,
        metadata={
            "name": "StepFreeAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    escalator_free_access: Optional[EscalatorFreeAccess] = field(
        default=None,
        metadata={
            "name": "EscalatorFreeAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    lift_free_access: Optional[LiftFreeAccess] = field(
        default=None,
        metadata={
            "name": "LiftFreeAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    audible_signals_available: Optional[AudibleSignalsAvailable] = field(
        default=None,
        metadata={
            "name": "AudibleSignalsAvailable",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    visual_signs_available: Optional[VisualSignsAvailable] = field(
        default=None,
        metadata={
            "name": "VisualSignsAvailable",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
