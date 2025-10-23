from dataclasses import dataclass, field
from typing import Optional
from ojp.accessibility_enumeration import AccessibilityEnumeration
from ojp.extensions_2 import Extensions2
from ojp.validity_condition_structure import ValidityConditionStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass
class AccessibilityLimitationStructure:
    """
    Type for limitation on navigation.

    :ivar limitation_id: Identifier of LIMITATION.
    :ivar validity_condition: Validty condition governing applicability
        of LIMITATION.
    :ivar wheelchair_access:
    :ivar step_free_access:
    :ivar escalator_free_access:
    :ivar lift_free_access:
    :ivar audible_signals_available: Whether a PLACE / SITE ELEMENT has
        Audible signals for the viusally impaired.
    :ivar visual_signs_available: Whether a PLACE / SITE ELEMENT has
        Visual signals for the hearing impaired.
    :ivar extensions:
    """
    limitation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "LimitationId",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        }
    )
    validity_condition: Optional[ValidityConditionStructure] = field(
        default=None,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        }
    )
    wheelchair_access: AccessibilityEnumeration = field(
        default=AccessibilityEnumeration.FALSE,
        metadata={
            "name": "WheelchairAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
            "required": True,
        }
    )
    step_free_access: Optional[AccessibilityEnumeration] = field(
        default=None,
        metadata={
            "name": "StepFreeAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        }
    )
    escalator_free_access: Optional[AccessibilityEnumeration] = field(
        default=None,
        metadata={
            "name": "EscalatorFreeAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        }
    )
    lift_free_access: Optional[AccessibilityEnumeration] = field(
        default=None,
        metadata={
            "name": "LiftFreeAccess",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        }
    )
    audible_signals_available: Optional[AccessibilityEnumeration] = field(
        default=None,
        metadata={
            "name": "AudibleSignalsAvailable",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        }
    )
    visual_signs_available: Optional[AccessibilityEnumeration] = field(
        default=None,
        metadata={
            "name": "VisualSignsAvailable",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/acsb",
        }
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        }
    )
