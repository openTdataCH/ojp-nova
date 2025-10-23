from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from nova.erstattungs_typ import ErstattungsTyp
from nova.geld_betrag import GeldBetrag
from nova.leistungs_typ import LeistungsTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class Savaktion:
    """
    Ein SAVProtokoll Eintrag liefert Angaben zu SAV-Leistungen, die zu einer
    verkauften Leistung erstellt wurden.

    :ivar sav_leistungs_id: Identifikation der zu dieser SAV-Aktion
        gehörenden SAV-Leistung.
    :ivar sav_leistungs_typ: Zeigt z.B. an ob es sich um eine
        Erstattung, Annullation oder (demnächst) eine Hinterlegung
        handelt.
    :ivar sav_erstattungs_typ: Zeigt z.B. an ob die OriginalLeistung
        komplett oder nur teilweise erstattet wurde.
    :ivar sav_grund: Grund der Durchführung der SAV-Aktion.
    :ivar sav_zeitpunkt: Zeitpunkt der Durchführung der SAV-Aktion.
    :ivar sav_verkaufs_preis: VerkaufsPreis der SAV-Leistung.
    :ivar anzahl_betroffene_leistungen: Anzahl Leistungen die mit der
        SAV-Leistung erstattet wurden.
    :ivar letzter_nutzungs_geltungs_tag: Letzter Tag, an welchem die
        Leistung nach zeitlicher Teilerstattung noch nutzbar ist.
    :ivar sav_gueltig_ab: Zeitpunkt ab dem sich die SAV-Aktion auf die
        OriginalLeistung auswirkt. Z.B. bei einer
        Teilerstattung/Hinterlegung eines Abonnements steht hier ab wann
        das Abonnement als erstattet/hinterlegt gilt.
    :ivar sav_gueltig_bis: Zeitpunkt bis zu dem sich die SAV-Aktion auf
        die OriginalLeistung auswirkt. Z.B. bei einer temporären
        Hinterlegung eines Abonnements steht hier bis wann das
        Abonnement als hinterlegt gilt.
    :ivar annullierte_savleistung: Bei Annullation einer zu dieser
        Leistung gehörenden SAV-Leistung: Identifikation der
        annullierten SAV-Leistung
    """
    class Meta:
        name = "SAVAktion"

    sav_leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "savLeistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    sav_leistungs_typ: Optional[LeistungsTyp] = field(
        default=None,
        metadata={
            "name": "savLeistungsTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    sav_erstattungs_typ: Optional[ErstattungsTyp] = field(
        default=None,
        metadata={
            "name": "savErstattungsTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    sav_grund: Optional[str] = field(
        default=None,
        metadata={
            "name": "savGrund",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    sav_zeitpunkt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "savZeitpunkt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    sav_verkaufs_preis: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "savVerkaufsPreis",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    anzahl_betroffene_leistungen: Optional[int] = field(
        default=None,
        metadata={
            "name": "anzahlBetroffeneLeistungen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    letzter_nutzungs_geltungs_tag: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "letzterNutzungsGeltungsTag",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    sav_gueltig_ab: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "savGueltigAb",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    sav_gueltig_bis: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "savGueltigBis",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    annullierte_savleistung: Optional[int] = field(
        default=None,
        metadata={
            "name": "annullierteSAVLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
