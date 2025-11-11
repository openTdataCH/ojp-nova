from dataclasses import dataclass, field
from typing import Optional

from ojp2.action_data_structure import ActionDataStructure
from ojp2.closed_timestamp_range_structure import ClosedTimestampRangeStructure
from ojp2.natural_language_string_structure import (
    NaturalLanguageStringStructure,
)
from ojp2.simple_action_structure import SimpleActionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ParameterisedActionStructure(SimpleActionStructure):
    """
    Type for parameterised, i.e. user definable, actions.

    :ivar description: Description of action.
    :ivar action_data: Data associated with action.
    :ivar publication_window: Defines a number of publication windows.
        When not sent, then the publication windows of higher level are
        valid. Can be overwritten by deeper level.
    """

    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    action_data: list[ActionDataStructure] = field(
        default_factory=list,
        metadata={
            "name": "ActionData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    publication_window: list[ClosedTimestampRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "PublicationWindow",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
