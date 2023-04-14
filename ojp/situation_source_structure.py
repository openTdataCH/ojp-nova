from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ojp.extensions_1 import Extensions1
from ojp.natural_language_string_structure import NaturalLanguageStringStructure
from ojp.situation_source_type_enumeration import SituationSourceTypeEnumeration
from ojp.source_type_enum import SourceTypeEnum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SituationSourceStructure:
    """
    Type for a source, i.e. provider of information.

    :ivar country: Country of origin of source element.
    :ivar source_type: Nature of Source.
    :ivar email: Email of Supplier of information.
    :ivar phone: Phone number of Supplier of information.
    :ivar fax: Fax number of Supplier of information.
    :ivar web: Information was obtained from a web site URL of site
        and/or page.
    :ivar other: Other information about source.
    :ivar source_method: Nature of method used to get Source.
    :ivar agent_reference: Reference to an Agent, i.e. Capture client
        user who input a SITUATION. Available for use in intranet
        exchange of SITUATIONs.
    :ivar name: Name of for source.
    :ivar source_role: Job title of Source.
    :ivar time_of_communication: Time of communication of message, if
        different from creation time.
    :ivar external_code: External system reference to SITUATION.
    :ivar source_file: Electronic file / attachment containing
        information about SITUATION.
    :ivar extensions:
    """
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    source_type: Optional[SituationSourceTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "SourceType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    phone: Optional[str] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    fax: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fax",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    web: Optional[str] = field(
        default=None,
        metadata={
            "name": "Web",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    other: Optional[str] = field(
        default=None,
        metadata={
            "name": "Other",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    source_method: Optional[SourceTypeEnum] = field(
        default=None,
        metadata={
            "name": "SourceMethod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    agent_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "AgentReference",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    source_role: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceRole",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    time_of_communication: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "TimeOfCommunication",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    external_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    source_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceFile",
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
