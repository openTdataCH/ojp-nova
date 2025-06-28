from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.cause import Cause
from ojp2.comment import Comment
from ojp2.confidentiality_value_enum import ConfidentialityValueEnum
from ojp2.extension_type import ExtensionType
from ojp2.group_of_locations import GroupOfLocations
from ojp2.impact import Impact
from ojp2.management import Management
from ojp2.probability_of_occurrence_enum import ProbabilityOfOccurrenceEnum
from ojp2.source import Source
from ojp2.url_link import UrlLink
from ojp2.validity import Validity

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class SituationRecord:
    situation_record_creation_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    situation_record_creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordCreationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    situation_record_observation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordObservationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    situation_record_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "situationRecordVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    situation_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    situation_record_first_supplier_version_time: Optional[XmlDateTime] = (
        field(
            default=None,
            metadata={
                "name": "situationRecordFirstSupplierVersionTime",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            },
        )
    )
    confidentiality_override: Optional[ConfidentialityValueEnum] = field(
        default=None,
        metadata={
            "name": "confidentialityOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    probability_of_occurrence: Optional[ProbabilityOfOccurrenceEnum] = field(
        default=None,
        metadata={
            "name": "probabilityOfOccurrence",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    validity: Optional[Validity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    impact: Optional[Impact] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    cause: Optional[Cause] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    general_public_comment: list[Comment] = field(
        default_factory=list,
        metadata={
            "name": "generalPublicComment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    non_general_public_comment: list[Comment] = field(
        default_factory=list,
        metadata={
            "name": "nonGeneralPublicComment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    url_link: list[UrlLink] = field(
        default_factory=list,
        metadata={
            "name": "urlLink",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    group_of_locations: Optional[GroupOfLocations] = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    management: Optional[Management] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    situation_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
