from dataclasses import dataclass, field
from typing import Optional

from ojp2.affects_scope_structure import AffectsScopeStructure
from ojp2.passenger_information_action import PassengerInformationAction
from ojp2.scope_type_enumeration import ScopeTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PublishingActionStructure:
    """
    Type for description of the whole action to be published (extends SIRI-SX
    v2.0p).

    :ivar publish_at_scope: Defines the information area where the
        action has to be published.
    :ivar passenger_information_action: Description of the whole
        passenger information of one action.
    """

    publish_at_scope: Optional["PublishingActionStructure.PublishAtScope"] = (
        field(
            default=None,
            metadata={
                "name": "PublishAtScope",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
    )
    passenger_information_action: list[PassengerInformationAction] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationAction",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )

    @dataclass
    class PublishAtScope:
        scope_type: Optional[ScopeTypeEnumeration] = field(
            default=None,
            metadata={
                "name": "ScopeType",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        affects: Optional[AffectsScopeStructure] = field(
            default=None,
            metadata={
                "name": "Affects",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
