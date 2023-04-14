from dataclasses import dataclass, field
from typing import Optional
from ojp.extension_type import ExtensionType
from ojp.situation_record import SituationRecord

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass
class GenericSituationRecord(SituationRecord):
    generic_situation_record_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "genericSituationRecordName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    generic_situation_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "genericSituationRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        }
    )
