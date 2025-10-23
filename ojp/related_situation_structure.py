from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ojp.extensions_1 import Extensions1
from ojp.iana_country_tld_enumeration import IanaCountryTldEnumeration
from ojp.related_to_enumeration import RelatedToEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class RelatedSituationStructure:
    """
    Type for a reference.

    :ivar creation_time: Time of creation of 'related to' assocation.
    :ivar country_ref: Unique identifier of a Country of a Participant
        who created SITUATION. Provides namespace for Participant If
        absent proided from context.
    :ivar participant_ref: Unique identifier of a Participant. Provides
        namespace for SITUATION. If absent provdied from context.
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
    :ivar external_reference: A single string that identifiers the
        referenced SITUATION.
    :ivar related_as: Relationship of refercence to the referncing
        SITUATION e.
    :ivar extensions:
    """
    creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CreationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    country_ref: Optional[IanaCountryTldEnumeration] = field(
        default=None,
        metadata={
            "name": "CountryRef",
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
    external_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalReference",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    related_as: Optional[RelatedToEnumeration] = field(
        default=None,
        metadata={
            "name": "RelatedAs",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
