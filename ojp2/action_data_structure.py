from dataclasses import dataclass, field
from typing import Optional

from ojp2.affects_scope_structure import AffectsScopeStructure
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.scope_type_enumeration import ScopeTypeEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ActionDataStructure:
    """
    Type for list of SITUATIONs.

    :ivar name: Name of action data Element.
    :ivar type_value: Data type of action data.
    :ivar value: Value for action.
    :ivar prompt: Display prompt for presenting action to user.
        (Unbounded since SIRI 2.0)
    :ivar publish_at_scope: Defines the information area where the
        action has to be published.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    value: list[object] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    prompt: list[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Prompt",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publish_at_scope: Optional["ActionDataStructure.PublishAtScope"] = field(
        default=None,
        metadata={
            "name": "PublishAtScope",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
