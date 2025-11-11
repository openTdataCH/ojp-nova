from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from ojp2.extension_type import ExtensionType
from ojp2.header_information import HeaderInformation
from ojp2.overall_severity_enum import OverallSeverityEnum
from ojp2.situation_record import SituationRecord

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class Situation:
    overall_severity: Optional[OverallSeverityEnum] = field(
        default=None,
        metadata={
            "name": "overallSeverity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    related_situation: list[str] = field(
        default_factory=list,
        metadata={
            "name": "relatedSituation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    situation_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "situationVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    situation_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "situationVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        },
    )
    situation_record: list[SituationRecord] = field(
        default_factory=list,
        metadata={
            "name": "situationRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    situation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "situationExtension",
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
