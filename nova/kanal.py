from dataclasses import dataclass, field
from typing import Optional
from nova.geschaefts_feld import GeschaeftsFeld
from nova.kanal_typ import KanalTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class Kanal:
    kanal_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "kanalCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "max_inclusive": 9999,
        }
    )
    kanal_typ: Optional[KanalTyp] = field(
        default=None,
        metadata={
            "name": "kanalTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    geschaefts_feld: Optional[GeschaeftsFeld] = field(
        default=None,
        metadata={
            "name": "geschaeftsFeld",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    bezeichnung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 200,
        }
    )
