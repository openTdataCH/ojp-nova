from dataclasses import dataclass, field
from typing import List, Optional
from nova.dauer import Dauer
from nova.erstattungs_grund_typ import ErstattungsGrundTyp
from nova.erstattungs_typ import ErstattungsTyp
from nova.geld_betrag import GeldBetrag
from nova.teil_erstattung_angabe import TeilErstattungAngabe
from nova.vermittler_einschraenkung import VermittlerEinschraenkung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ErstattungsBedingung:
    """
    :ivar moeglicher_erstattungs_grund:
    :ivar anwendungs_einschraenkungen:
    :ivar selbst_behalt_vor_beginn_gueltigkeit:
    :ivar selbst_behalt_nach_beginn_gueltigkeit:
    :ivar id:
    :ivar bezeichnung:
    :ivar erstattungs_typ: VOLLERSTATTUNG, TEILERSTATTUNG, ANNULLATION
    :ivar benoetigte_angaben:
    :ivar selbst_behalt_uebersteuerbar:
    """
    moeglicher_erstattungs_grund: List[ErstattungsGrundTyp] = field(
        default_factory=list,
        metadata={
            "name": "moeglicherErstattungsGrund",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_occurs": 1,
        }
    )
    anwendungs_einschraenkungen: Optional["ErstattungsBedingung.AnwendungsEinschraenkungen"] = field(
        default=None,
        metadata={
            "name": "anwendungsEinschraenkungen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    selbst_behalt_vor_beginn_gueltigkeit: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "selbstBehaltVorBeginnGueltigkeit",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    selbst_behalt_nach_beginn_gueltigkeit: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "selbstBehaltNachBeginnGueltigkeit",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    bezeichnung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 200,
        }
    )
    erstattungs_typ: Optional[ErstattungsTyp] = field(
        default=None,
        metadata={
            "name": "erstattungsTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    benoetigte_angaben: Optional[TeilErstattungAngabe] = field(
        default=None,
        metadata={
            "name": "benoetigteAngaben",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    selbst_behalt_uebersteuerbar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "selbstBehaltUebersteuerbar",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )

    @dataclass
    class AnwendungsEinschraenkungen:
        zeitraum_fuer_erstattung_nach_kauf: Optional[Dauer] = field(
            default=None,
            metadata={
                "name": "zeitraumFuerErstattungNachKauf",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            }
        )
        zeitraum_fuer_erstattung_nach_ende_gueltigkeit: Optional[Dauer] = field(
            default=None,
            metadata={
                "name": "zeitraumFuerErstattungNachEndeGueltigkeit",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            }
        )
        erstattbar_vor_beginn_gueltigkeit: Optional[bool] = field(
            default=None,
            metadata={
                "name": "erstattbarVorBeginnGueltigkeit",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
                "required": True,
            }
        )
        erstattbar_nach_beginn_gueltigkeit: Optional[bool] = field(
            default=None,
            metadata={
                "name": "erstattbarNachBeginnGueltigkeit",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
                "required": True,
            }
        )
        traeger_medium_original_leistung: List[str] = field(
            default_factory=list,
            metadata={
                "name": "traegerMediumOriginalLeistung",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
                "min_length": 0,
                "max_length": 50,
            }
        )
        zahlungsart_nicht_erlaubt: List[str] = field(
            default_factory=list,
            metadata={
                "name": "zahlungsartNichtErlaubt",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
                "min_length": 0,
                "max_length": 50,
            }
        )
        vermittler_einschraenkung: List[VermittlerEinschraenkung] = field(
            default_factory=list,
            metadata={
                "name": "vermittlerEinschraenkung",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            }
        )
