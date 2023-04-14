from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nova.geschlecht import Geschlecht
from nova.leistungs_info import LeistungsInfo
from nova.reisenden_typ_code import ReisendenTypCode
from nova.verbund_leistungs_info import VerbundLeistungsInfo

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ReisendenInfo:
    """
    Dieses Objekt enthält Informationen zum Reisenden, die einen Einfluss auf
    die Angebotsbestimmung haben.

    :ivar mit_tkid:
    :ivar ohne_tkid:
    :ivar reisenden_beziehung: KEINE_FAMILIENBEZIEHUNG;
        ELTERNTEIL_REIST_MIT; GROSSELTERNTEIL_REIST_MIT;
        ERWACHSENER_REIST_MIT
    :ivar vorhandene_leistungen: @Deprecated Replaced by
        vorhandeneVerbundLeistung. Will be removed in NOVA 15.
    :ivar vorhandene_verbund_leistung:
    :ivar externe_reisenden_referenz_id:
    """
    mit_tkid: Optional["ReisendenInfo.MitTkid"] = field(
        default=None,
        metadata={
            "name": "mitTkid",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    ohne_tkid: Optional["ReisendenInfo.OhneTkid"] = field(
        default=None,
        metadata={
            "name": "ohneTkid",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    reisenden_beziehung: List[str] = field(
        default_factory=list,
        metadata={
            "name": "reisendenBeziehung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    vorhandene_leistungen: List[LeistungsInfo] = field(
        default_factory=list,
        metadata={
            "name": "vorhandeneLeistungen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    vorhandene_verbund_leistung: List[VerbundLeistungsInfo] = field(
        default_factory=list,
        metadata={
            "name": "vorhandeneVerbundLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    externe_reisenden_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeReisendenReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )

    @dataclass
    class MitTkid:
        """
        :ivar tkid:
        :ivar ermaessigungs_karte_code: HTA; KEINE_ERMAESSIGUNGSKARTE;
            JUNIORKARTE; ENKELKARTE; EURAIL_CH_1KL; EURAIL_CH_2KL;
            GA_1KL; GA_2KL; INTERRAIL_CH_1KL; INTERRAIL_CH_2KL;
            ST_PASS_1KL; ST_PASS_2KL
        """
        tkid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "length": 36,
                "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
            }
        )
        ermaessigungs_karte_code: List[str] = field(
            default_factory=list,
            metadata={
                "name": "ermaessigungsKarteCode",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_length": 0,
                "max_length": 50,
            }
        )

    @dataclass
    class OhneTkid:
        """
        :ivar reisenden_typ:
        :ivar geschlecht:
        :ivar alter:
        :ivar geburts_tag:
        :ivar ermaessigungs_karte_code: HTA; KEINE_ERMAESSIGUNGSKARTE;
            JUNIORKARTE; ENKELKARTE; EURAIL_CH_1KL; EURAIL_CH_2KL;
            GA_1KL; GA_2KL; INTERRAIL_CH_1KL; INTERRAIL_CH_2KL;
            ST_PASS_1KL; ST_PASS_2KL
        """
        reisenden_typ: Optional[ReisendenTypCode] = field(
            default=None,
            metadata={
                "name": "reisendenTyp",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
        geschlecht: Optional[Geschlecht] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        alter: Optional[int] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_inclusive": 0,
                "max_inclusive": 200,
            }
        )
        geburts_tag: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "geburtsTag",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        ermaessigungs_karte_code: List[str] = field(
            default_factory=list,
            metadata={
                "name": "ermaessigungsKarteCode",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_occurs": 1,
                "min_length": 0,
                "max_length": 50,
            }
        )
