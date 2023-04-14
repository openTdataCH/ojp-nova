from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ojp.abstract_situation_element_structure import AbstractSituationElementStructure
from ojp.references_structure import ReferencesStructure
from ojp.situation_source_structure import SituationSourceStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SituationElementStructure(AbstractSituationElementStructure):
    """
    Type for loggable Entry.

    :ivar references: Associations with other SITUATIONs.
    :ivar source: Information about source of information, that is,
        where the agent using the capture client obtained an item of
        information, or in the case of an automated feed, an identifier
        of the specific feed. Can be used to obtain updates, verify
        details or otherwise assess relevance.
    :ivar versioned_at_time: Time at which SITUATION element was
        versioned. Once versioned, no furtr changes can be made.
    """
    references: Optional[ReferencesStructure] = field(
        default=None,
        metadata={
            "name": "References",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    source: Optional[SituationSourceStructure] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    versioned_at_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "VersionedAtTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
