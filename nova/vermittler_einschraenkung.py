from dataclasses import dataclass, field
from typing import List, Optional
from nova.kanal_typ import KanalTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VermittlerEinschraenkung:
    """
    :ivar verkaufs_kanal_typ: AUTOMAT, ONLINE, BEDIENTER_VERKAUF, BATCH
    :ivar leistungs_vermittler:
    :ivar erstattungs_lvgleich_verkaufs_lv:
    :ivar verkaufs_kanal_code:
    :ivar verkaufs_stelle:
    :ivar vertriebs_punkt:
    :ivar verkaufs_geraete_id:
    """
    verkaufs_kanal_typ: List[KanalTyp] = field(
        default_factory=list,
        metadata={
            "name": "verkaufsKanalTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    leistungs_vermittler: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsVermittler",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "max_inclusive": 99999,
        }
    )
    erstattungs_lvgleich_verkaufs_lv: Optional[bool] = field(
        default=None,
        metadata={
            "name": "erstattungsLVgleichVerkaufsLV",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    verkaufs_kanal_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "verkaufsKanalCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "max_inclusive": 9999,
        }
    )
    verkaufs_stelle: Optional[int] = field(
        default=None,
        metadata={
            "name": "verkaufsStelle",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "max_inclusive": 99999,
        }
    )
    vertriebs_punkt: Optional[int] = field(
        default=None,
        metadata={
            "name": "vertriebsPunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "max_inclusive": 99999,
        }
    )
    verkaufs_geraete_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "verkaufsGeraeteId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 1,
            "max_length": 50,
            "pattern": r"[0-9a-zA-Z_\-]+",
        }
    )
