from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class RollenZugriff:
    kanal_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "kanalCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "max_inclusive": 9999,
        }
    )
    leistungs_vermittler: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsVermittler",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "max_inclusive": 99999,
        }
    )
    verkaufs_geraete_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "verkaufsGeraeteId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 1,
            "max_length": 50,
            "pattern": r"[0-9a-zA-Z_\-]+",
        }
    )
    verkaufs_stelle: Optional[int] = field(
        default=None,
        metadata={
            "name": "verkaufsStelle",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "max_inclusive": 99999,
        }
    )
    vertriebs_punkt: Optional[int] = field(
        default=None,
        metadata={
            "name": "vertriebsPunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "max_inclusive": 99999,
        }
    )
