from dataclasses import dataclass, field
from typing import List
from ojp.related_situation_structure import RelatedSituationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ReferencesStructure:
    """
    Type for references.

    :ivar related_to_ref: A reference to another SITUATION with an
        indication of the nature of the association, e.g. a cause, a
        result, an update. Note that a Entry that is an update, i.e. has
        the same IdentifierNumber but a later version number as a
        previous Entry alway has a supercedes relationship and this does
        not need to be expliciitly coded.
    """
    related_to_ref: List[RelatedSituationStructure] = field(
        default_factory=list,
        metadata={
            "name": "RelatedToRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
