from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nova.dauer import Dauer
from nova.gueltigkeits_zeitraum import GueltigkeitsZeitraum
from nova.leistungs_anrechnung import LeistungsAnrechnung
from nova.tarif_stufe import TarifStufe
from nova.verbindung import Verbindung
from nova.zeitraum import Zeitraum

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class NutzungsInfo:
    """
    Liefert Informationen zur Nutzung eines Angebots wie Geltungstage und
    -zeiten.

    :ivar tarif_stufe: @Deprecated Ersetzt durch
        AbstractAngebot/AbstractLeistung.tarifStufe. Wird in NOVA 15
        entfernt.
    :ivar vorverkaufs_frist:
    :ivar verbindung:
    :ivar entwertungs_zeitraum:
    :ivar nutzungs_zeitraum:
    :ivar angerechnete_leistung: An ein Anschlussbillett angerechnete
        Leistung.
    :ivar anzahl_einheiten:
    :ivar restliche_einheiten:
    :ivar erster_nutzungs_geltungs_tag: Wird nur für Angebote (1. Klang)
        geliefert.
    :ivar gruppen_name: Nur bei Gruppenangeboten
    :ivar gruppe_anzahl_total: Nur bei Gruppenangeboten: Gesamtanzahl
        Reisender in der Gruppe
    :ivar gruppe_anzahl_gratis: Nur bei Gruppenangeboten: Anzahl
        Reisender, die gratis reisen.
    """
    tarif_stufe: Optional[TarifStufe] = field(
        default=None,
        metadata={
            "name": "tarifStufe",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    vorverkaufs_frist: Optional[Dauer] = field(
        default=None,
        metadata={
            "name": "vorverkaufsFrist",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    verbindung: List[Verbindung] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    entwertungs_zeitraum: Optional[Zeitraum] = field(
        default=None,
        metadata={
            "name": "entwertungsZeitraum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    nutzungs_zeitraum: List[GueltigkeitsZeitraum] = field(
        default_factory=list,
        metadata={
            "name": "nutzungsZeitraum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_occurs": 2,
        }
    )
    angerechnete_leistung: List[LeistungsAnrechnung] = field(
        default_factory=list,
        metadata={
            "name": "angerechneteLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    anzahl_einheiten: Optional[int] = field(
        default=None,
        metadata={
            "name": "anzahlEinheiten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 9999,
        }
    )
    restliche_einheiten: Optional[int] = field(
        default=None,
        metadata={
            "name": "restlicheEinheiten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    erster_nutzungs_geltungs_tag: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ersterNutzungsGeltungsTag",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    gruppen_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "gruppenName",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )
    gruppe_anzahl_total: Optional[int] = field(
        default=None,
        metadata={
            "name": "gruppeAnzahlTotal",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 999,
        }
    )
    gruppe_anzahl_gratis: Optional[int] = field(
        default=None,
        metadata={
            "name": "gruppeAnzahlGratis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 999,
        }
    )
