from dataclasses import dataclass, field
from typing import Optional
from nova.kanal import Kanal

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VerkaeuferInformation:
    verkaufs_kanal: Optional[Kanal] = field(
        default=None,
        metadata={
            "name": "verkaufsKanal",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    leistungs_vermittler: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsVermittler",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 99999,
        }
    )
    verkaufs_stelle: Optional[int] = field(
        default=None,
        metadata={
            "name": "verkaufsStelle",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 99999,
        }
    )
    vertriebs_punkt: Optional[int] = field(
        default=None,
        metadata={
            "name": "vertriebsPunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 99999,
        }
    )
    verkaufs_geraete_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "verkaufsGeraeteId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 1,
            "max_length": 50,
            "pattern": r"[0-9a-zA-Z_\-]+",
        }
    )
