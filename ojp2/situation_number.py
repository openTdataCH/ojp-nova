from dataclasses import dataclass

from ojp2.entry_qualifier_structure import EntryQualifierStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SituationNumber(EntryQualifierStructure):
    """Identifier of SITUATION within a Participant.

    Exclude versionr.
    """

    class Meta:
        namespace = "http://www.siri.org.uk/siri"
