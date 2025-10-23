from dataclasses import dataclass, field
from typing import List, Optional
from nova.reise_weg_info import ReiseWegInfo
from nova.strecken_tarif_strecke import StreckenTarifStrecke
from nova.strecken_weg_meta_daten import StreckenWegMetaDaten
from nova.verbund_tarif_strecke import VerbundTarifStrecke
from nova.verkehrs_strecke import VerkehrsStrecke

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class StreckenGeltungsBereich:
    """
    Für Leistungen wird der StreckenbereichGeltungsbereich nur geliefert, wenn
    dieser VerbundTarifStrecken (Lang- oder Kurzstrecke) abdeckt.

    :ivar reise_weg_info:
    :ivar strecken_weg_meta_daten:
    :ivar verkehrs_strecke: wird nur im 1. Klang befüllt
    :ivar strecken_tarif_strecke:
    :ivar verbund_tarif_strecke:
    """
    reise_weg_info: List[ReiseWegInfo] = field(
        default_factory=list,
        metadata={
            "name": "reiseWegInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    strecken_weg_meta_daten: Optional[StreckenWegMetaDaten] = field(
        default=None,
        metadata={
            "name": "streckenWegMetaDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    verkehrs_strecke: List[VerkehrsStrecke] = field(
        default_factory=list,
        metadata={
            "name": "verkehrsStrecke",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    strecken_tarif_strecke: List[StreckenTarifStrecke] = field(
        default_factory=list,
        metadata={
            "name": "streckenTarifStrecke",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    verbund_tarif_strecke: Optional[VerbundTarifStrecke] = field(
        default=None,
        metadata={
            "name": "verbundTarifStrecke",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
