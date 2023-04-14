from dataclasses import dataclass, field
from typing import Optional
from ojp.iana_country_tld_enumeration import IanaCountryTldEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SituationFullRefStructure1:
    """
    Type for reference to a SITUATION.

    :ivar version_country_ref: Unique identifier of a Country of a
        Participant who created Update SITUATION element. Provides
        namespace for VersionParticipant If absent same as.
    :ivar participant_ref: Unique identifier of a Participant. Provides
        namespace for SITUATION.
    :ivar situation_number: Unique identifier of SITUATION within a
        Participant. Excludes any version number.
    :ivar update_country_ref: Unique identifier of a Country of a
        Participant who created Update SITUATION element. Provides
        namespace for VersionParticipant If absent same as.
    :ivar update_participant_ref: Unique identifier of a Participant.
        Provides namespace for SITUATION. If absent provdied from
        context.
    :ivar version: Unique identifier of update version within a
        SITUATION Number Omit if reference to the base SITUATION.
    """
    class Meta:
        name = "SituationFullRefStructure"

    version_country_ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "name": "VersionCountryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    situation_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SituationNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    update_country_ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "name": "UpdateCountryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    update_participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "UpdateParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
