from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from ojp.parameterised_action_structure import ParameterisedActionStructure
from ojp.perspective_enumeration import PerspectiveEnumeration
from ojp.textual_content_structure import TextualContentStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class PassengerInformationActionStructure(ParameterisedActionStructure):
    """
    :ivar action_ref: Reference to the action number within the incident
        concept.
    :ivar recorded_at_time: The time of the last update. This must be
        the timestamp of the original data source and not that of an
        intermediate system, such as a data hub. This timestamp has to
        be changed by the source system with every update.
    :ivar version: The monotonically inscresing version of the passenger
        information instance. If absent, is the same version as the
        enclosing Situation
    :ivar source_ref: The system which created this passenger
        information. If absent, the same system as the
        PtSituationElement.ParticipantRef.
    :ivar owner_ref: The organisation which owns this passenger
        information.
    :ivar perspective: Perspective of the passenger, e.g. general,
        vehicleJourney, stopPoint.
    :ivar action_priority: Prioritises a passenger information action
        from the information owner's point of view, e.g. suitable for
        sorting or hiding individual passenger information actions. 1 =
        highest priority.
    :ivar textual_content: The actual, structured passenger information
        for a specific TextualContentSize.
    """
    action_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    recorded_at_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "RecordedAtTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    version: Optional[int] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    source_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    owner_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "OwnerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    perspective: List[PerspectiveEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Perspective",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
    action_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActionPriority",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    textual_content: List[TextualContentStructure] = field(
        default_factory=list,
        metadata={
            "name": "TextualContent",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
