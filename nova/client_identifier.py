from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class ClientIdentifier:
    """
    Ein ClientIdentfier identifiziert den anfragenden Client (Serviceaufrufer)
    aus fachlicher Sicht.

    :ivar leistungs_vermittler:
    :ivar kanal_code:
    :ivar verkaufs_stelle:
    :ivar vertriebs_punkt:
    :ivar verkaufs_geraete_id:
    :ivar bearbeiter: Benutzername oder Referenz des Bearbeiters
    """
    leistungs_vermittler: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsVermittler",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "max_inclusive": 99999,
        }
    )
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
    verkaufs_stelle: Optional[int] = field(
        default=None,
        metadata={
            "name": "verkaufsStelle",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    vertriebs_punkt: Optional[int] = field(
        default=None,
        metadata={
            "name": "vertriebsPunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    verkaufs_geraete_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "verkaufsGeraeteId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 1,
            "max_length": 50,
            "pattern": r"[0-9a-zA-Z_\-]+",
        }
    )
    bearbeiter: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 64,
        }
    )
