from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime
from nova.nova_base import (
    ClientIdentifier,
    CorrelationKontext,
    DatumsZeitraum,
    Dauer,
    GeldBetrag,
    Geschlecht,
    Kanal,
    LocalizedString,
    Meldungen,
    Operator,
    PagingParameter,
    Preis,
    SprachCode,
    SystemInformation,
    TimeShift,
    WochenTag,
    ZahlungsIntervall,
    Zeitraum,
)
from nova.nova_vertriebs_base import (
    AngebotsFilter,
    AusweisbarerZeitraum,
    DruckBeleg,
    ErneuerungsArt,
    ErneuerungsArtGrund,
    ErstattungsGrundTyp as NovaVertriebsBaseErstattungsGrundTyp,
    ErstattungsTyp,
    FahrArtTypCode,
    FahrAusweisArt,
    GenerischerEinflussFaktorTyp,
    GenerischerEinflussFaktorWert,
    KlassenTypCode,
    Parkplatz,
    RabattKlasse,
    ReiseWegInfo,
    ReisendenTypCode,
    StreckenWegMetaDaten,
    VerbundStreckenTyp,
    VerkaufsParameterTyp,
    VerkaufsParameterWert,
    VerkehrsMittelTypCode,
    WegAngabe,
    ZahlungsArt,
    ZahlungsAttribut,
    ZeitlicheFlexibilitaet,
)

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AbstractRabattType:
    pass


class AnfrageProtokollLevel(Enum):
    OFF = "OFF"
    SUMMARY = "SUMMARY"
    INFO = "INFO"
    DEBUG = "DEBUG"


class AusgabeStatusTyp(Enum):
    NICHT_GEDRUCKT = "NICHT_GEDRUCKT"
    DRUCK_ERFOLGREICH = "DRUCK_ERFOLGREICH"
    DRUCK_ERFOLGREICH_IMMUTABLE = "DRUCK_ERFOLGREICH_IMMUTABLE"


@dataclass
class B2BrabattStufeCodeListe:
    """
    Liste von möglichen B2B-RabattstufeCodes.
    """
    class Meta:
        name = "B2BRabattStufeCodeListe"

    b2b_rabatt_stufe_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "b2bRabattStufeCode",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
            "min_length": 0,
            "max_length": 32,
        }
    )


class BefahrungsTyp(Enum):
    RAUMZEIT = "RAUMZEIT"
    STRECKEZEIT = "STRECKEZEIT"


@dataclass
class FahrplanVerbindungsHaltestelle:
    """Die Verbindungshaltestelle ist ein Halt innerhalb eines Verbindungssegments
    zu einer bestimmten Zeit an einem bestimmten Ort.

    Eine Verbindungshaltestelle definiert die Ankunfts- und Abfahrtszeit einer Verbindung an einer bestimmten angefahrenen Haltestelle. Mitternachtsüberschreitungen: Eine Mitternachtsüberschreitung liegt für ein VerbindungsSegment dann vor, wenn das Segment am Tag n startet und am Tag n + 1 endet. Eine Mitternachtsüberschreitung kann stattfinden:
    - an einer VerbindungsHaltestelle, wenn die Abfahrtszeit und Ankunftszeit nicht am selben Tag liegen. - zwischen zwei aufeinander folgenden Haltestellen, wenn die Abfahrtszeit an einer Haltestelle nicht am selben Tag liegt wie die Ankunftszeit der folgenden VerbindungsHaltestelle.
    Es gibt Spezialfalle, bei denen für die VerbindungsHaltestelle keine Zeiten vorliegen. z.B. sind für VerbindungsHaltestelle, welche zu einem Verbindungssegment für Fusswege (Gattung = Walk) gehören oder virtuelle Haltestellen repräsentieren.
    """
    abfahrts_zeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "abfahrtsZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    ankunfts_zeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ankunftsZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    haltestelle: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )


class FahrtWunschAbdeckung(Enum):
    HINFAHRT = "HINFAHRT"
    RUECKFAHRT = "RUECKFAHRT"
    RETOUR = "RETOUR"


@dataclass
class FreizeitBeleg:
    payload: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "format": "base64",
        }
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeType",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    freizeit_traeger_medium_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "freizeitTraegerMediumCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class FreizeitBelegParameter:
    """
    :ivar code: z.B. für Ausweisnummer und Postleitzahl SwissPass
    :ivar wert:
    """
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    wert: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class GruppenReiseInfoRequest:
    """
    :ivar anzahl:
    :ivar kunden_segment_code:
    :ivar ist_reise_leiter_kunden_segment: @Deprecated Will be removed
        in NOVA 15.
    """
    anzahl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 999,
        }
    )
    kunden_segment_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "kundenSegmentCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    ist_reise_leiter_kunden_segment: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istReiseLeiterKundenSegment",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


class KaufArt(Enum):
    ERSTKAUF = "ERSTKAUF"
    FOLGEKAUF = "FOLGEKAUF"


class Komfort(Enum):
    KLASSE_1 = "KLASSE_1"
    KLASSE_2 = "KLASSE_2"


class KontrollElementFormat(Enum):
    PNG = "PNG"
    RAW = "RAW"


@dataclass
class LeistungsFachSchluessel:
    """
    :ivar leistungs_id:
    :ivar leistungs_referenz:
    :ivar sicherheits_element_id: ID, wie vom SicherheitselementService
        vergeben.
    :ivar leistungs_paket_id:
    :ivar erneuerungs_id: UUID der Leistung, die in der URL im
        ErneurungsInfoService verwendet wird
    :ivar kunden_name:
    :ivar kunden_vorname:
    :ivar kunden_geburts_datum:
    """
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    leistungs_referenz: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsReferenz",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    sicherheits_element_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "sicherheitsElementId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 20,
        }
    )
    leistungs_paket_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsPaketId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 1,
            "max_length": 37,
        }
    )
    erneuerungs_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "erneuerungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    kunden_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "kundenName",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 30,
        }
    )
    kunden_vorname: Optional[str] = field(
        default=None,
        metadata={
            "name": "kundenVorname",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 30,
        }
    )
    kunden_geburts_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "kundenGeburtsDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


class LeistungsStatus(Enum):
    """
    Der Leistungsstatus ist eine Enum und kann die Werte OFFERIERT,VERKAUFT,
    PRODUKTION_BEREIT, PRODUKTION_ERFOLGREICH, TECHNISCH_STORNIERT und
    NICHT_VERKAUFT annehmen.
    """
    OFFERIERT = "OFFERIERT"
    VERKAUFT = "VERKAUFT"
    PRODUKTION_BEREIT = "PRODUKTION_BEREIT"
    PRODUKTION_ERFOLGREICH = "PRODUKTION_ERFOLGREICH"
    TECHNISCH_STORNIERT = "TECHNISCH_STORNIERT"
    NICHT_VERKAUFT = "NICHT_VERKAUFT"


class LeistungsTypCode(Enum):
    """
    Enum der möglichen Typen von Leistungen.
    """
    VERKAUF = "VERKAUF"
    ERSTATTUNG = "ERSTATTUNG"
    ANNULLATION = "ANNULLATION"
    ANNULLATION_ERSTATTUNG = "ANNULLATION_ERSTATTUNG"
    HINTERLEGUNG = "HINTERLEGUNG"
    AKTIVIERUNG = "AKTIVIERUNG"


class Paketbedingung(Enum):
    NUR_ZUSAMMEN_KAUFBAR = "NUR_ZUSAMMEN_KAUFBAR"
    SEPARATER_KAUF_MOEGLICH = "SEPARATER_KAUF_MOEGLICH"
    NUR_MIT_BESTEHENDEM_FAHRAUSWEIS = "NUR_MIT_BESTEHENDEM_FAHRAUSWEIS"


@dataclass
class ProduktRabattType:
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    rabatt_stufe_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "rabattStufeCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 32,
        }
    )


class PruefStatus(Enum):
    GUELTIG_HINREICHEND = "GUELTIG_HINREICHEND"
    GUELTIG_NICHT_HINREICHEND = "GUELTIG_NICHT_HINREICHEND"
    UNGUELTIG = "UNGUELTIG"
    MANUELL_ZU_PRUEFEN = "MANUELL_ZU_PRUEFEN"
    NICHT_GEPRUEFT = "NICHT_GEPRUEFT"


class RaeumlicheFlexibilitaet(Enum):
    VERBINDUNG = "VERBINDUNG"
    STRECKE = "STRECKE"
    ZONEN = "ZONEN"
    STRECKE_UND_ZONEN = "STRECKE_UND_ZONEN"
    VERBUND = "VERBUND"
    NATIONAL = "NATIONAL"


@dataclass
class Reisender:
    """
    Repräsentiert in einer Angebotsantwort einen Reisenden.
    """
    meldungen_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "meldungenRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "tokens": True,
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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


class SavTyp(Enum):
    ERSTATTUNG = "ERSTATTUNG"
    ANNULLATION = "ANNULLATION"
    ANNULLATION_ERSTATTUNG = "ANNULLATION_ERSTATTUNG"
    HINTERLEGUNG = "HINTERLEGUNG"
    ENTSCHAEDIGUNG = "ENTSCHAEDIGUNG"
    SPERRUNG_NUTZUNG = "SPERRUNG_NUTZUNG"
    SPERRUNG_ERSTATTUNG = "SPERRUNG_ERSTATTUNG"
    ENTSPERRUNG_NUTZUNG = "ENTSPERRUNG_NUTZUNG"
    ENTSPERRUNG_ERSTATTUNG = "ENTSPERRUNG_ERSTATTUNG"


class SperrTyp(Enum):
    """
    Enumeration aller Typen von Sperren.
    """
    NUTZUNG = "NUTZUNG"
    ERSTATTUNG = "ERSTATTUNG"
    HINTERLEGUNG = "HINTERLEGUNG"


@dataclass
class Strecke:
    """
    Die Klasse Strecke ist die abstrakte Basisklasse für alle Arten von Strecken
    (Wege oder Fahrplanverbindungen).
    """


@dataclass
class StreckenTarifStrecke:
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class TeilErstattung:
    """Das Objekt Teilerstattung kann Teil einer ErstattungsAngebotsanfrage sein.

    Eine Teilerstattung enthält (optional) Informationen zu:
    - der Anzahl benutzter Einheiten Leistung der ErstattungsAngebotsanfrage - dem gewünschten Erstattungsdatum
    """
    letztes_gueltigkeits_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "letztesGueltigkeitsDatum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    anzahl_genutzte_einheiten: Optional[int] = field(
        default=None,
        metadata={
            "name": "anzahlGenutzteEinheiten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 9999,
        }
    )
    angebot_id_benutzter_teil: Optional[str] = field(
        default=None,
        metadata={
            "name": "angebotIdBenutzterTeil",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "length": 37,
            "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )


class TransaktionsVerhalten(Enum):
    COMMIT_ON_ERROR = "COMMIT_ON_ERROR"
    ROLLBACK_ON_ERROR = "ROLLBACK_ON_ERROR"


@dataclass
class VerkehrsMittelGattung:
    """
    VerkehrsMittel mit Code (und Nummer) pro Verbindungssegment.
    """
    gattungs_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "gattungsCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    verkehrs_mittel_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "verkehrsMittelNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


class WegPosition(Enum):
    ANFANG = "ANFANG"
    UNTERWEGS = "UNTERWEGS"
    ENDE = "ENDE"


@dataclass
class Zone:
    """Repräsentiert eine Zone eines Tarifverbunds in der ein Ticket gültig ist.

    Zonen kommen bei der Tarifierung von Verbunds- und City-Tickets zur
    Anwendung. Eine Zone wird durch einen Code sowie passender
    Bezeichnung identifiziert.
    """
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    bezeichnung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )
    ist_lokalnetz: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istLokalnetz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    zonen_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "zonenOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )


@dataclass
class ZonenBuendelRequest:
    zone: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    alle_zonen: Optional[bool] = field(
        default=None,
        metadata={
            "name": "alleZonen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    tarif_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "tarifOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )


@dataclass
class ZonenRequest:
    """
    :ivar zone:
    :ivar alle_zonen:
    :ivar tarif_owner:
    :ivar abgangs_haltestelle: Nur bei Strecke-Zeit-Verbunden (TNW)
        erforderlich.
    """
    zone: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    alle_zonen: Optional[bool] = field(
        default=None,
        metadata={
            "name": "alleZonen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    tarif_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "tarifOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    abgangs_haltestelle: Optional[int] = field(
        default=None,
        metadata={
            "name": "abgangsHaltestelle",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )


class ZwischenHaltContextTripContext(Enum):
    PLANNED = "PLANNED"
    UNPLANNED = "UNPLANNED"
    IRRELEVANT = "IRRELEVANT"
    CANCELLED = "CANCELLED"


@dataclass
class AngebotVerkaufsParameterType:
    verkaufs_parameter: Optional[VerkaufsParameterTyp] = field(
        default=None,
        metadata={
            "name": "verkaufsParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    vorgabe_wert: Optional[VerkaufsParameterWert] = field(
        default=None,
        metadata={
            "name": "vorgabeWert",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    optional: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class AngebotsDruckDaten:
    beleg: List[DruckBeleg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    angebots_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "angebotsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "length": 37,
            "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )


@dataclass
class AngebotsPaket:
    """Ein AngebotsPaket, welches Alternativ- und/oder optionale Zusatzangebote
    beinhaltet, referenziert alle AngebotsPakete wofür das alternative
    AngebotsPaket eine Alternative oder Ergänzung (Zusatzangebote) ist.

    AngebotsPakete werden von NOVA nicht sortiert - diese Aufgabe liegt an LV

    :ivar angebot_refs: Verweist auf 1..* Angebote/SAVAngebote, die
        gemeinsam ein AngebotsPaket darstellen und gemeinsam gekauft
        werden sollten, um den Kundenwunsch abzudecken.
    :ivar reisender_refs: Verweist auf Reisende, für die dieses Angebot
        gültig ist.
    :ivar meldungen_refs:
    :ivar id:
    :ivar paketbedingung:
    """
    angebot_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "angebotRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "tokens": True,
        }
    )
    reisender_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "reisenderRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "tokens": True,
        }
    )
    meldungen_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "meldungenRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "tokens": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    paketbedingung: Optional[Paketbedingung] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class B2BrabattType(AbstractRabattType):
    class Meta:
        name = "B2BRabattType"

    rabatt_stufe_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "rabattStufeCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 32,
        }
    )


@dataclass
class ErstattungsDaten:
    """
    Enthält Erstattungsangaben für eine OriginalLeistung.

    :ivar erstattungs_betrag:
    :ivar preis_benutzter_teil: @Deprecated replaced with benutzterTeil
        element. Will be removed in NOVA 15.
    :ivar benutzter_teil:
    :ivar erstattungs_grund:
    :ivar letzter_nutzungs_geltungs_tag:
    :ivar erstattungs_typ:
    :ivar entschaedigung_datum:
    """
    erstattungs_betrag: Optional[Preis] = field(
        default=None,
        metadata={
            "name": "erstattungsBetrag",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    preis_benutzter_teil: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "preisBenutzterTeil",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    benutzter_teil: Optional[Preis] = field(
        default=None,
        metadata={
            "name": "benutzterTeil",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    erstattungs_grund: Optional[NovaVertriebsBaseErstattungsGrundTyp] = field(
        default=None,
        metadata={
            "name": "erstattungsGrund",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    letzter_nutzungs_geltungs_tag: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "letzterNutzungsGeltungsTag",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    erstattungs_typ: Optional[ErstattungsTyp] = field(
        default=None,
        metadata={
            "name": "erstattungsTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    entschaedigung_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "entschaedigungDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class ErstattungsGrundTyp:
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class FahrplanVerbindungsSegment:
    """Ein Verbindungssegment entspricht einer (Teil)-Verbindung, auf welcher die
    Verwaltung, Gattung (resp.

    Nummer) gleich bleibt. Typischerweise werden beim Umsteigen auf ein
    anderes VerkehrsMittel mehrere Verbindungssegmente benötigt.

    :ivar verkehrs_mittel:
    :ivar zwischen_halt:
    :ivar zwischen_halt_context:
    :ivar einstieg: Für das erste Segment immer gefüllt.
    :ivar ausstieg: Für das letzte Segment immer gefüllt.
    :ivar verwaltungs_code:
    :ivar info_plus_tarif_code:
    :ivar abfahrts_zeit: Auf dem ersten FahrplanverbindungsSegment muss
        eine Abfahrtszeit gesetzt sein.
    :ivar ankunfts_zeit: Auf dem letzten FahrplanverbindungsSegment muss
        eine Ankunftszeit gesetzt sein.
    """
    verkehrs_mittel: Optional[VerkehrsMittelGattung] = field(
        default=None,
        metadata={
            "name": "verkehrsMittel",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    zwischen_halt: List[int] = field(
        default_factory=list,
        metadata={
            "name": "zwischenHalt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    zwischen_halt_context: List["FahrplanVerbindungsSegment.ZwischenHaltContext"] = field(
        default_factory=list,
        metadata={
            "name": "zwischenHaltContext",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    einstieg: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    ausstieg: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    verwaltungs_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "verwaltungsCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    info_plus_tarif_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "infoPlusTarifCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    abfahrts_zeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "abfahrtsZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    ankunfts_zeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ankunftsZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class ZwischenHaltContext:
        uic_code: Optional[int] = field(
            default=None,
            metadata={
                "name": "uicCode",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_inclusive": 0,
            }
        )
        trip_context: Optional[ZwischenHaltContextTripContext] = field(
            default=None,
            metadata={
                "name": "tripContext",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )


@dataclass
class FreizeitRabattType(AbstractRabattType):
    produkt_rabatt: List[ProduktRabattType] = field(
        default_factory=list,
        metadata={
            "name": "produktRabatt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )


@dataclass
class GeltungsDauerProduktEinflussFaktor:
    entwertungs_zeitraum: Optional[Dauer] = field(
        default=None,
        metadata={
            "name": "entwertungsZeitraum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    nutzungs_geltungs_dauer: Optional[Dauer] = field(
        default=None,
        metadata={
            "name": "nutzungsGeltungsDauer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class GenerischerProduktEinflussFaktor:
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    wert_bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "wertBezeichnung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    wert: Optional[GenerischerEinflussFaktorWert] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    typ: Optional[GenerischerEinflussFaktorTyp] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class GueltigkeitsZeitraum:
    """Kombination des tarifierbaren und ausweisbaren Zeitraums.

    AusweisbarerZeitraum darf lediglich zu Ausgabezwecken (Druck / Screenanzeige) verwendet werden. In der Business-Logik (z.B. beim Vergleich von Gültigkeitszeiträumen) muss der tarifierbareZeitraum verwendet werden! Beispiel: DV-Einzelbillett 125 - tarifarischer Nutzungszeitraum = 24.08.2016, 00:00:00 Uhr – 25.08.2016 05:00:00 Uhr (29 Stunden, bis 5 Uhr am Folgetag) - ausgewiesener Nutzungszeitraum = 24.08.2016 – 24.08.2016 (1 Tag, ohne Zeitangabe)
    """
    tarifierbarer_zeitraum: Optional[Zeitraum] = field(
        default=None,
        metadata={
            "name": "tarifierbarerZeitraum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    ausweisbarer_zeitraum: Optional[AusweisbarerZeitraum] = field(
        default=None,
        metadata={
            "name": "ausweisbarerZeitraum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    reisezeit_toleranz: Optional[Dauer] = field(
        default=None,
        metadata={
            "name": "reisezeitToleranz",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class Kante:
    """
    Eine Kante verbindet zwei Haltestellen im Verkehrsnetz.
    """
    von: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    nach: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    verkehrs_mittel_typ: Optional[VerkehrsMittelTypCode] = field(
        default=None,
        metadata={
            "name": "verkehrsMittelTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class KontrollElementParameter:
    """
    :ivar sprache: Moegliche Werte: DE, EN, IT, FR
    :ivar format: Moegliche Werte: PNG, RAW
    """
    sprache: Optional[SprachCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    format: Optional[KontrollElementFormat] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class KontrollStatus:
    """
    :ivar kontroll_zeitpunkt: Datum und Zeit wann die Kontrolle
        durchgeführt wurde.
    :ivar tco_code: Partner-Code der kontrollierenden
        Transportunternehmung
    :ivar kurs_nummer: Kurs-Nummer des VerkehrsMittels, in welchem die
        Kontrolle stattgefunden hat (z.B. Zugnummer).
    :ivar kontroll_person: Kürzel der kontrollierenden Person.
    :ivar resultat_auto: Resultat von automatischer Kontrolle. Wird
        durch Kontrollgerät vorgeschlagen. Hinweis: kann durch
        Kontrollperson übersteuert werden (s. resultatManuell)
    :ivar resultat_manuell: Resultat von Kontrolle. Wird durch
        Kontrollperson gewählt.
    """
    kontroll_zeitpunkt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "kontrollZeitpunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    tco_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "tcoCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 99999,
        }
    )
    kurs_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "kursNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )
    kontroll_person: Optional[str] = field(
        default=None,
        metadata={
            "name": "kontrollPerson",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )
    resultat_auto: Optional[PruefStatus] = field(
        default=None,
        metadata={
            "name": "resultatAuto",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    resultat_manuell: Optional[PruefStatus] = field(
        default=None,
        metadata={
            "name": "resultatManuell",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class KundenSegmentProduktEinflussFaktor:
    """
    Beschreibt als Spezialisierung eines Produkteinflussfaktors ein spezifisches
    KundenSegment (1/1, ?, Erwachsene, Ermassigt).

    :ivar bezeichnung:
    :ivar kunden_segment_code: Code kann über Stammdaten zu den
        relevanten Attributen (min/max Alter, reisendenTyp,
        ermaessigungsKarte etc.) aufgelöst werden.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    kunden_segment_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "kundenSegmentCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class LeistungErstattungsRequest:
    teil_erstattung: Optional[TeilErstattung] = field(
        default=None,
        metadata={
            "name": "teilErstattung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    erstattungs_grund: Optional[str] = field(
        default=None,
        metadata={
            "name": "erstattungsGrund",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class LeistungVerkaufsParameterType:
    wert: Optional[VerkaufsParameterWert] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class LeistungsInfo:
    """Leistungen die nicht über die TKID definiert werden können (z.B.

    Abonnemente auf Sicherheitspapier), aber für die korrekte
    Tarifierung von Anschlussbilletten verwendet werden können.

    :ivar zonen_geltungs_bereich: Jede Leistung mit Zonegültigkeit hat
        i.d.R. einen zonenGeltungsBereich. Ausnahme: Gewisse
        Fahrausweise die in Zonen unterschiedlicher Verbunde gültig sind
        haben pro Verbund einen eigenen zonenGeltungsBereich.
    :ivar leistungs_info_id: Identifier der manuell angegebenen
        Leistung: kann entweder NOVA LeistungsID oder ein beliebiger
        anderer Identifier sein.
    :ivar gueltig_von:
    :ivar gueltig_bis:
    :ivar produkt_nummer:
    :ivar klasse:
    """
    zonen_geltungs_bereich: Optional["LeistungsInfo.ZonenGeltungsBereich"] = field(
        default=None,
        metadata={
            "name": "zonenGeltungsBereich",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    leistungs_info_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsInfoId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    gueltig_von: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigVon",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    gueltig_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    klasse: Optional[KlassenTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )

    @dataclass
    class ZonenGeltungsBereich:
        zone: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_length": 0,
                "max_length": 50,
            }
        )
        alle_zonen: Optional[bool] = field(
            default=None,
            metadata={
                "name": "alleZonen",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        tarif_stufen_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "tarifStufenCode",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_length": 0,
                "max_length": 50,
            }
        )


@dataclass
class LeistungsInfoType:
    """
    Leistung die an ein Anschlussbillett angerechnet wurde.

    :ivar leistungs_id: Identifier einer NOVA-Leistung.
    :ivar externe_leistungs_referenz_id: Identifier einer Leistung die
        nicht über NOVA verkauft wurde.
    :ivar gueltigkeit:
    :ivar zonen_geltungs_bereich: Jede Leistung mit Zonegültigkeit hat
        i.d.R. einen zonenGeltungsBereich. Ausnahme: Gewisse
        Fahrausweise die in Zonen unterschiedlicher Verbunde gültig sind
        haben pro Verbund einen eigenen zonenGeltungsBereich.
    :ivar tarif_owner:
    :ivar produkt_nummer:
    :ivar klasse:
    """
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    externe_leistungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeLeistungsReferenzId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    gueltigkeit: List[Zeitraum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zonen_geltungs_bereich: List["LeistungsInfoType.ZonenGeltungsBereich"] = field(
        default_factory=list,
        metadata={
            "name": "zonenGeltungsBereich",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    tarif_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "tarifOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    klasse: Optional[KlassenTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class ZonenGeltungsBereich:
        zone: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_length": 0,
                "max_length": 50,
            }
        )
        alle_zonen: Optional[bool] = field(
            default=None,
            metadata={
                "name": "alleZonen",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )


@dataclass
class LeistungsSucheFeld:
    """@Deprecated Will be removed in NOVA 15.

    :ivar such_begriff: Suchbegriff, nach welchem im Feldname gesucht
        wird. Werden mehrere Suchbegriffe angegeben, so werden diese
        ODER-verknüpft. Hinweis: Datum/Zeit-Werte werden als String
        analog zum Format xs:dateTime angegeben.
    :ivar key: Schlüssel des Leistungs-Feldes, welches durchsucht werden
        soll. Hinweis: die möglichen Keys werden in einer separaten
        Liste publiziert.
    :ivar operator: Definiert, wie im Feld nach dem Suchbegriff gesucht
        wird (z.B. gleich, grösser oder gleich, kleiner oder gleich).
    """
    such_begriff: List[str] = field(
        default_factory=list,
        metadata={
            "name": "suchBegriff",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    operator: Optional[Operator] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class LeistungsTyp:
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    code: Optional[LeistungsTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class RabattAnfrageType:
    rabatt: List[AbstractRabattType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )


@dataclass
class RabattInfoType:
    rabatt_preis: Optional[Preis] = field(
        default=None,
        metadata={
            "name": "rabattPreis",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    rabatt_klasse: Optional[RabattKlasse] = field(
        default=None,
        metadata={
            "name": "rabattKlasse",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    in_verkaufs_preis_eingerechnet: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inVerkaufsPreisEingerechnet",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    rabatt_stufe_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "rabattStufeCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 32,
        }
    )


@dataclass
class SavprotokollEintrag:
    """
    Ein SAVProtokoll Eintrag liefert Angaben zu SAV-Leistungen, die zu einer
    verkauften Leistung erstellt wurden.

    :ivar sav_leistungs_id: Identifikation der zu dieser SAV-Aktion
        gehörenden SAV-Leistung.
    :ivar sav_typ: Zeigt z.B. an ob es sich um eine Erstattung,
        Annullation, Hinterlegung oder eine Sperrung handelt.
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
        name = "SAVProtokollEintrag"

    sav_leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "savLeistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    sav_typ: Optional[SavTyp] = field(
        default=None,
        metadata={
            "name": "savTyp",
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
        }
    )
    sav_grund: Optional[str] = field(
        default=None,
        metadata={
            "name": "savGrund",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
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


@dataclass
class StornierungsInfo:
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    leistungs_status: Optional[LeistungsStatus] = field(
        default=None,
        metadata={
            "name": "leistungsStatus",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class StreckenSperre:
    """
    :ivar meldung_ref: @Deprecated Will be removed in NOVA 15. Use
        "meldungRefs" instead.
    :ivar meldung_refs:
    :ivar umsteige_punkt_uic:
    :ivar strecken_sperre_gueltigkeiten: List contains information about
        the durations of a Streckensperre. Multiple child elements means
        AND
    """
    meldung_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "meldungRef",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    meldung_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "meldungRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "tokens": True,
        }
    )
    umsteige_punkt_uic: List[int] = field(
        default_factory=list,
        metadata={
            "name": "umsteigePunktUIC",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    strecken_sperre_gueltigkeiten: Optional["StreckenSperre.StreckenSperreGueltigkeiten"] = field(
        default=None,
        metadata={
            "name": "streckenSperreGueltigkeiten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )

    @dataclass
    class StreckenSperreGueltigkeiten:
        strecken_sperre_gueltigkeit: List["StreckenSperre.StreckenSperreGueltigkeiten.StreckenSperreGueltigkeit"] = field(
            default_factory=list,
            metadata={
                "name": "streckenSperreGueltigkeit",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_occurs": 1,
            }
        )

        @dataclass
        class StreckenSperreGueltigkeit:
            """
            :ivar wochen_tage: Weeks days within begin and end when the
                streckenSperre is active. "wochenTage" limits "beginn"
                and "ende" to the explicit week days defined.
            :ivar sperr_zeiten: Times within begin and end andweek days
                when the Streckensperre is active. "sperrZeiten" limits
                the Streckensperre to the explicit times defined here.
            :ivar beginn:
            :ivar ende:
            """
            wochen_tage: Optional["StreckenSperre.StreckenSperreGueltigkeiten.StreckenSperreGueltigkeit.WochenTage"] = field(
                default=None,
                metadata={
                    "name": "wochenTage",
                    "type": "Element",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                }
            )
            sperr_zeiten: Optional["StreckenSperre.StreckenSperreGueltigkeiten.StreckenSperreGueltigkeit.SperrZeiten"] = field(
                default=None,
                metadata={
                    "name": "sperrZeiten",
                    "type": "Element",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                }
            )
            beginn: Optional[XmlDateTime] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                    "required": True,
                }
            )
            ende: Optional[XmlDateTime] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                    "required": True,
                }
            )

            @dataclass
            class WochenTage:
                wochen_tag: List[WochenTag] = field(
                    default_factory=list,
                    metadata={
                        "name": "wochenTag",
                        "type": "Element",
                        "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                        "min_occurs": 1,
                    }
                )

            @dataclass
            class SperrZeiten:
                sperr_zeit: List["StreckenSperre.StreckenSperreGueltigkeiten.StreckenSperreGueltigkeit.SperrZeiten.SperrZeit"] = field(
                    default_factory=list,
                    metadata={
                        "name": "sperrZeit",
                        "type": "Element",
                        "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                        "min_occurs": 1,
                    }
                )

                @dataclass
                class SperrZeit:
                    beginn_zeit: Optional[XmlTime] = field(
                        default=None,
                        metadata={
                            "name": "beginnZeit",
                            "type": "Element",
                            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                            "required": True,
                        }
                    )
                    ende_zeit: Optional[XmlTime] = field(
                        default=None,
                        metadata={
                            "name": "endeZeit",
                            "type": "Element",
                            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                            "required": True,
                        }
                    )


@dataclass
class TarifStufe:
    """Die Tarifstufe gibt die Anzahl Zonen an, die für die Preisberechnung
    zugrunde gelegt wurden.

    Die Anzahl der Zonen aus der Tarifstufe deckt sich nicht zwingend
    mit der Anzahl der Zonen, die tatsächlich befahren werden dürfen.
    Eine Tarifstufe kann aber auch "Alle Zonen" oder "Kurzstrecke" sein.
    """
    tarif_stufen_text: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "tarifStufenText",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    tarif_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "tarifOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    anzahl_tarifierte_zonen: Optional[int] = field(
        default=None,
        metadata={
            "name": "anzahlTarifierteZonen",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    tarif_stufen_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "tarifStufenCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class Verbindung:
    gattung: Optional[VerkehrsMittelGattung] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    abgang: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    bestimmung: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    abfahrts_zeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "abfahrtsZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    ankunfts_zeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ankunftsZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class VerbundLeistungsInfo:
    """
    :ivar leistungs_id: @Deprecated Wird in NOVA 15 entfernt. Bitte das
        Element verbundLeistung befüllen.
    :ivar verbund_leistung:
    """
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    verbund_leistung: Optional["VerbundLeistungsInfo.VerbundLeistung"] = field(
        default=None,
        metadata={
            "name": "verbundLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class VerbundLeistung:
        """Verbund-Leistung die nicht mit einer TKID verknüpft ist (z.B.

        Abonnement auf Sicherheitspapier), aber für die korrekte
        Tarifierung von Anschlussbilletten verwendet werden kann.
        """
        verbund_code: Optional[int] = field(
            default=None,
            metadata={
                "name": "verbundCode",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "max_inclusive": 99999,
            }
        )
        produkt_nummer: Optional[int] = field(
            default=None,
            metadata={
                "name": "produktNummer",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_inclusive": 0,
            }
        )
        zonen_geltungs_bereich: Optional["VerbundLeistungsInfo.VerbundLeistung.ZonenGeltungsBereich"] = field(
            default=None,
            metadata={
                "name": "zonenGeltungsBereich",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
        externe_leistungs_referenz_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "externeLeistungsReferenzId",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_length": 0,
                "max_length": 50,
            }
        )
        klasse: Optional[KlassenTypCode] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
        gueltig_von: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "gueltigVon",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        gueltig_bis: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "gueltigBis",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )

        @dataclass
        class ZonenGeltungsBereich:
            zone: List[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                    "min_length": 0,
                    "max_length": 50,
                }
            )
            alle_zonen: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "alleZonen",
                    "type": "Element",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                }
            )


@dataclass
class VerbundStreckenRequest:
    """
    :ivar tarif_owner:
    :ivar strecken_typ: KURZSTRECKE; LANGSTRECKE
    :ivar abgangs_haltestelle:
    """
    tarif_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "tarifOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    strecken_typ: Optional[VerbundStreckenTyp] = field(
        default=None,
        metadata={
            "name": "streckenTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    abgangs_haltestelle: Optional[int] = field(
        default=None,
        metadata={
            "name": "abgangsHaltestelle",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )


@dataclass
class VerbundTarifStrecke:
    strecken_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "streckenOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    strecken_typ: Optional[VerbundStreckenTyp] = field(
        default=None,
        metadata={
            "name": "streckenTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    befahrungs_typ: Optional[BefahrungsTyp] = field(
        default=None,
        metadata={
            "name": "befahrungsTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    abgang: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )


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


@dataclass
class VertragsDaten:
    beleg: Optional[DruckBeleg] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )


@dataclass
class VertragsInfo:
    mindest_vertrags_dauer: Optional[Dauer] = field(
        default=None,
        metadata={
            "name": "mindestVertragsDauer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    ist_neuer_vertrag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istNeuerVertrag",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    kauf_art: Optional[KaufArt] = field(
        default=None,
        metadata={
            "name": "kaufArt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    erneuerungs_art: Optional[ErneuerungsArt] = field(
        default=None,
        metadata={
            "name": "erneuerungsArt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    erneuerungs_art_grund: Optional[ErneuerungsArtGrund] = field(
        default=None,
        metadata={
            "name": "erneuerungsArtGrund",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    vertrags_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "vertragsNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 10,
        }
    )
    kauf_auf_rechnung_moeglich: Optional[bool] = field(
        default=None,
        metadata={
            "name": "kaufAufRechnungMoeglich",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    vertrags_scan_vorhanden: Optional[bool] = field(
        default=None,
        metadata={
            "name": "vertragsScanVorhanden",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zahlungs_intervall: Optional[ZahlungsIntervall] = field(
        default=None,
        metadata={
            "name": "zahlungsIntervall",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    vertrags_partner: Optional[str] = field(
        default=None,
        metadata={
            "name": "vertragsPartner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    basis_vertrags_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "basisVertragsNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 10,
        }
    )
    bestehende_vertrags_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "bestehendeVertragsNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 10,
        }
    )


@dataclass
class VertriebsRequest:
    """
    Abstrakte Basisklasse aller Anfragen, welche der NOVA Vertriebsservice entgegen
    nimmt.
    """
    client_identifier: Optional[ClientIdentifier] = field(
        default=None,
        metadata={
            "name": "clientIdentifier",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    correlation_kontext: Optional[CorrelationKontext] = field(
        default=None,
        metadata={
            "name": "correlationKontext",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    time_shift: Optional[TimeShift] = field(
        default=None,
        metadata={
            "name": "timeShift",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    fachlog_level: Optional[AnfrageProtokollLevel] = field(
        default=None,
        metadata={
            "name": "fachlogLevel",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class VertriebsResponse:
    """
    :ivar meldungen:
    :ivar anfrage_protokoll_id:
    :ivar daten_release_id: Gibt die DatenRelease-ID an, die bei der
        Bearbeitung der Anfrage verwendet wurde.
    """
    meldungen: Optional[Meldungen] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    anfrage_protokoll_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "anfrageProtokollId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    daten_release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "datenReleaseId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 100,
        }
    )


@dataclass
class WegSuche(Strecke):
    """Die Klasse dient zur Formulierung von streckenbasierten Angebotsanfragen auf
    Basis eines Wegs.

    In diesem Fall führt die öV-Plattform selbst eine Wegsuche basierend
    auf dem übergebenen Weg durch.

    :ivar weg_suche_segment:
    :ivar folge_haltestelle: Mobile Verkaufsstellen können die noch
        abzufahrenden Haltestellen mitgeben.
    :ivar datum_hin_fahrt:
    :ivar zeitpunkt_hin_fahrt:
    :ivar nur_hin_fahrt_anbieten:
    :ivar zeit_spanne_weg_suche_minuten: Beschränkt die für eine
        Wegsuche verwendeten Fahrplanverbindungen auf den Zeitraum
        [zeitpunktHinFahrt, zeitpunktHinFahrt +
        zeitspanneWegsucheMinuten]. Darf nur gemeinsam mit
        zeitpunktHinFahrt angegeben werden und muss grösser 0 sein.
    """
    weg_suche_segment: List["WegSuche.WegSucheSegment"] = field(
        default_factory=list,
        metadata={
            "name": "wegSucheSegment",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    folge_haltestelle: List[int] = field(
        default_factory=list,
        metadata={
            "name": "folgeHaltestelle",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    datum_hin_fahrt: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "datumHinFahrt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    zeitpunkt_hin_fahrt: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "zeitpunktHinFahrt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    nur_hin_fahrt_anbieten: bool = field(
        default=False,
        metadata={
            "name": "nurHinFahrtAnbieten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zeit_spanne_weg_suche_minuten: Optional[int] = field(
        default=None,
        metadata={
            "name": "zeitSpanneWegSucheMinuten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 9999,
        }
    )

    @dataclass
    class WegSucheSegment:
        verkehrs_mittel_typ: List[VerkehrsMittelTypCode] = field(
            default_factory=list,
            metadata={
                "name": "verkehrsMittelTyp",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        abgang: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_inclusive": 0,
            }
        )
        bestimmung: Optional[int] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_inclusive": 0,
            }
        )


@dataclass
class WertProduktEinflussFaktor:
    label: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    wert: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class ZahlungsInformation:
    """Die ZahlungsInformation beinhaltet Angaben zum Zahlungsmittel, mit dem eine
    Leistung bezahlt wurde.

    ZahlungsInformationen beinhalten zum heutigen Stand nur die
    Zahlungsart (bar, Visa, Master,...). Nicht enthalten ist das
    konkrete Zahlungsmittel (bspw. Kreditkartennummer).

    :ivar zahlungs_art:
    :ivar geld_betrag: Der Anteil am Gesamtbetrag der Leistung, der mit
        der Zahlungsart bezahlt wurde.
    :ivar zahlungs_attribut: Beliebige Attribute, die ein LV zu einem
        Zahlvorgang abspeichern kann. Wird z.B: von B2B verwendet, um in
        gewissen Situationen die RechnungsStelle und die Kostenzuordnung
        zu übergeben.
    :ivar externe_zahlungs_referenz: Kann von den LV verwendet werden,
        um eine Referenz auf ihren Zahlvorgang abzulegen.
    """
    zahlungs_art: Optional[ZahlungsArt] = field(
        default=None,
        metadata={
            "name": "zahlungsArt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    geld_betrag: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "geldBetrag",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    zahlungs_attribut: List[ZahlungsAttribut] = field(
        default_factory=list,
        metadata={
            "name": "zahlungsAttribut",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    externe_zahlungs_referenz: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeZahlungsReferenz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )


@dataclass
class ZahlungsInformationRequest:
    """
    Die ZahlungsInformationAnfrage dient als Container für die
    ZahlungsInformationen.

    :ivar geld_betrag: Der Anteil am Gesamtbetrag der Leistung, der mit
        der Zahlungsartart bezahlt wurde.
    :ivar zahlungs_attribut: Beliebige Attribute, die ein LV zu einem
        Zahlvorgang abspeichern kann. Wird z.B: von B2B verwendet, um in
        gewissen Situationen die RechnungsStelle und die Kostenzuordnung
        zu übergeben.
    :ivar zahlungs_art_code: UNBEKANNT; BAR; BON; MAE; FAK; DOS; DIN;
        AMX; JCB; VEG; VIS; PCD; YWD; MC; EC; MIG; ONE; REK; UAP
    :ivar externe_zahlungs_referenz: Kann von den LV verwendet werden,
        um eine Referenz auf ihren Zahlvorgang abzulegen.
    """
    geld_betrag: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "geldBetrag",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    zahlungs_attribut: List[ZahlungsAttribut] = field(
        default_factory=list,
        metadata={
            "name": "zahlungsAttribut",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zahlungs_art_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "zahlungsArtCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    externe_zahlungs_referenz: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeZahlungsReferenz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )


@dataclass
class ZonenBuendel:
    """Ein Zonenbündel beinhaltet Zonen, die gemeinsam (im Bündel) angeboten werden
    (z.B.

    die Libero Zonen 100+101 [Kern- und Ringzone Bern])

    :ivar zone:
    :ivar additive_zone:
    :ivar bezeichnung: Die Bezeichnung von Zonbenbündeln wird u.a. für
        Modul-Abo Zonen oder City-Zonen gesetzt (z.B. City-Zone Bern).
        Für Verbundtickets üblicherweise nicht gesetzt.
    :ivar weg_position:
    :ivar pflicht_zonen_buendel: Kennzeichnet, ob es sich bei den im
        Zonenbündel enthaltenen Zonen um Pflichtzonen handelt, die
        zwingender Bestandteil des Angebots sind.
    :ivar alle_zonen: Kennzeichnet, ob der Geltungsbereich "ALLE ZONEN"
        des TarifOwners umfasst. Default ist false. Wenn true, werden
        keine (additiven) Zonen geliefert.
    :ivar tarif_owner:
    :ivar befahrungs_typ:
    :ivar nova_zonen_tarif_code:
    """
    zone: List[Zone] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    additive_zone: List[Zone] = field(
        default_factory=list,
        metadata={
            "name": "additiveZone",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    weg_position: Optional[WegPosition] = field(
        default=None,
        metadata={
            "name": "wegPosition",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    pflicht_zonen_buendel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "pflichtZonenBuendel",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    alle_zonen: Optional[bool] = field(
        default=None,
        metadata={
            "name": "alleZonen",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    tarif_owner: Optional[int] = field(
        default=None,
        metadata={
            "name": "tarifOwner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    befahrungs_typ: Optional[BefahrungsTyp] = field(
        default=None,
        metadata={
            "name": "befahrungsTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    nova_zonen_tarif_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "novaZonenTarifCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 255,
        }
    )


@dataclass
class Ping:
    class Meta:
        name = "ping"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    client_identifier: Optional[ClientIdentifier] = field(
        default=None,
        metadata={
            "name": "clientIdentifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PingResponse:
    class Meta:
        name = "pingResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    system_information: Optional[SystemInformation] = field(
        default=None,
        metadata={
            "name": "systemInformation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AbstractAngebot:
    """
    Superklasse für Angebote und SAVAngebote.

    :ivar meldungen_refs:
    :ivar verkaufs_parameter:
    :ivar verkaufs_preis:
    :ivar tarif_stufe: Gesetzt bei Verbund-Fahrausweisen. i.d.R. 1
        Taristufe. Ausnahme: Bei gewissen Fahrausweisen die in Zonen
        unterschiedlicher Verbunde gültig sind wird pro Verbund eine
        eigene Tarifstufe ausgewiesen.
    :ivar rabatt_info:
    :ivar info_text_id:
    :ivar angebotskombination:
    :ivar angebots_id: ID, die ein Angebot eindeutig identifiziert. Die
        ID ist im 2. Klang zur Identifikation des Angebots zu verwenden.
        Ausnahme: Bei ErneuerungsInfoAngebotAntwort werden die Angebote
        nicht persisitiert und können daher im 2. Klang nicht verwendet
        werden.
    :ivar generation_stich_datum: Datum/Zeit des angewendeten
        Preisberechnungszeitpunkt und damit der DatenRelease-Zeitscheibe
        (Verkaufs- o. Reisezeitpunkt)
    :ivar produkt_nummer:
    :ivar vorhalte_zeitpunkt_bis: Zeitpunkt bis zu dem das Angebot
        gespeichert wird und von Operationen die auf Angeboten operieren
        (wie z.B. offeriereLeistungen, kaufeAngebote,
        liefereBelegeFuerAngebot etc.) verarbeitet werden kann.
    """
    meldungen_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "meldungenRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "tokens": True,
        }
    )
    verkaufs_parameter: List[AngebotVerkaufsParameterType] = field(
        default_factory=list,
        metadata={
            "name": "verkaufsParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    verkaufs_preis: Optional[Preis] = field(
        default=None,
        metadata={
            "name": "verkaufsPreis",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    tarif_stufe: List[TarifStufe] = field(
        default_factory=list,
        metadata={
            "name": "tarifStufe",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    rabatt_info: List[RabattInfoType] = field(
        default_factory=list,
        metadata={
            "name": "rabattInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    info_text_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "infoTextId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )
    angebotskombination: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    angebots_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "angebotsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "length": 37,
            "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    generation_stich_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "generationStichDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    vorhalte_zeitpunkt_bis: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "vorhalteZeitpunktBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class AngebotBewertungsInfo:
    """Liefert (nicht normative) Informationen, die Vermittlern eine Bewertung
    eines Angebots ermöglichen.

    Alle Felder einer AngebotBewertungsInfo sind optional. Ein Feld ist
    IMMER gesetzt, wenn die entsprechende Bewertungsdimension für das
    vorliegende Produkt relevant ist (z.B. alle Felder bei 125er und den
    meisten anderen Billett-Produkten). Ist die Dimension nicht relevant
    (z.B. raeumlicheFlexibilitaet beim Produkt Elvia-Reiseversicherung),
    so wird das Feld nicht gesetzt.
    """
    zeitliche_flexibilitaet: Optional[ZeitlicheFlexibilitaet] = field(
        default=None,
        metadata={
            "name": "zeitlicheFlexibilitaet",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    strecken_sperre: List[StreckenSperre] = field(
        default_factory=list,
        metadata={
            "name": "streckenSperre",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    raeumliche_flexibilitaet: Optional[RaeumlicheFlexibilitaet] = field(
        default=None,
        metadata={
            "name": "raeumlicheFlexibilitaet",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    komfort: Optional[Komfort] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    reisenden_beziehung: Optional[str] = field(
        default=None,
        metadata={
            "name": "reisendenBeziehung",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    teil_angebot: Optional[bool] = field(
        default=None,
        metadata={
            "name": "teilAngebot",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class AngebotsBelegRequest(VertriebsRequest):
    """
    Das Objekt Beleganfrage dient als Container für alle Informationen, die
    notwendig sind, um für die übermittelten angebotsId eine AngebotsBelegantwort
    zu liefern.
    """
    angebots_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "angebotsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
            "length": 37,
            "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )


@dataclass
class AngebotsBelegResponse(VertriebsResponse):
    """Die AngebotsBelegantwort ist das Antwortsobjekt fuer
    liefereBelegeFuerAngebot.

    Sie enthält für jede übermittelte AngebotsId ein Objekt
    AngebotsDruckDaten in dem alle bereits für das Angebot vorliegenden
    Druckattribute enthalten sind. Dies sind u.U. nicht alle
    Druckattribute (z.B. Sicherheitselement, LeistungsId, Zahlmittel
    fehlen).
    """
    angebots_druck_daten: List[AngebotsDruckDaten] = field(
        default_factory=list,
        metadata={
            "name": "angebotsDruckDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class AngebotsKaufRequestParam:
    """
    :ivar verkaufs_parameter:
    :ivar zahlungs_information:
    :ivar angebots_id: Angebots-ID, die bei erstelleAngebote geliefert
        wurde.
    :ivar leistungs_referenz:
    :ivar externe_leistungs_referenz_id: Für den ClientIdentifier
        (Vermittler) eindeutige ID der verkauften Leistung zur
        angebotsId. Dient der Zuordnung im Fehlerfall und bei
        wiederholtem Aufruf.
    :ivar verkaufs_zeitpunkt: Optionale Angabe des Verkaufszeitpunkts.
        Wird dann so in die erstellte NOVA Leistung übernommen.
    :ivar externe_reisenden_referenz_id:
    """
    verkaufs_parameter: List[LeistungVerkaufsParameterType] = field(
        default_factory=list,
        metadata={
            "name": "verkaufsParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zahlungs_information: List[ZahlungsInformationRequest] = field(
        default_factory=list,
        metadata={
            "name": "zahlungsInformation",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    angebots_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "angebotsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "length": 37,
            "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    leistungs_referenz: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsReferenz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    externe_leistungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeLeistungsReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    verkaufs_zeitpunkt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "verkaufsZeitpunkt",
            "type": "Attribute",
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
class BelegRequest(VertriebsRequest):
    """
    Das Objekt Beleganfrage dient als Container für alle Informationen, die
    notwendig sind, um für die übermittelte leistungsId eine Belegantwort zu
    liefern.
    """
    leistungs_id: List[int] = field(
        default_factory=list,
        metadata={
            "name": "leistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
            "min_inclusive": 0,
        }
    )
    kontroll_element_parameter: Optional[KontrollElementParameter] = field(
        default=None,
        metadata={
            "name": "kontrollElementParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    transaktions_verhalten: Optional[TransaktionsVerhalten] = field(
        default=None,
        metadata={
            "name": "transaktionsVerhalten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class BestaetigeProduktionRequest(VertriebsRequest):
    """
    Diese Klasse dient als Container für alle zu bestätigenden Leistungen.
    """
    leistungs_id: List[int] = field(
        default_factory=list,
        metadata={
            "name": "leistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
            "min_inclusive": 0,
        }
    )
    transaktions_verhalten: Optional[TransaktionsVerhalten] = field(
        default=None,
        metadata={
            "name": "transaktionsVerhalten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class ErneuerungsRequest:
    """
    :ivar bestehende_leistungs_id:
    :ivar externe_leistungs_referenz_id:
    :ivar original_leistung_produkt_nummer:
    :ivar original_leistung_gueltig_bis:
    :ivar vertrags_partner_tkid:
    :ivar reisender_tkid:
    :ivar vertrags_nummer:
    :ivar original_leistung_klasse:
    :ivar original_leistungs_erster_lv:
    :ivar rabatt_request:
    :ivar gueltig_ab:
    :ivar ersatz_leistungs_kauf: Attribut zur Steuerung des
        Ersatzleistungskaufs. Wird für interne Zwecke benötigt.
    """
    bestehende_leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "bestehendeLeistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    externe_leistungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeLeistungsReferenzId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    original_leistung_produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "originalLeistungProduktNummer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    original_leistung_gueltig_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "originalLeistungGueltigBis",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    vertrags_partner_tkid: Optional[str] = field(
        default=None,
        metadata={
            "name": "vertragsPartnerTkid",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    reisender_tkid: Optional[str] = field(
        default=None,
        metadata={
            "name": "reisenderTkid",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    vertrags_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "vertragsNummer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 10,
        }
    )
    original_leistung_klasse: Optional[int] = field(
        default=None,
        metadata={
            "name": "originalLeistungKlasse",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    original_leistungs_erster_lv: Optional[int] = field(
        default=None,
        metadata={
            "name": "originalLeistungsErsterLV",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 99999,
        }
    )
    rabatt_request: Optional[RabattAnfrageType] = field(
        default=None,
        metadata={
            "name": "rabattRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    gueltig_ab: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "gueltigAb",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    ersatz_leistungs_kauf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ersatzLeistungsKauf",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class ErstatteteLeistung:
    original_preis: Optional[Preis] = field(
        default=None,
        metadata={
            "name": "originalPreis",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    erstattungs_daten: Optional[ErstattungsDaten] = field(
        default=None,
        metadata={
            "name": "erstattungsDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    zahlungs_information: List[ZahlungsInformation] = field(
        default_factory=list,
        metadata={
            "name": "zahlungsInformation",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    leistungs_paket_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsPaketId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 1,
            "max_length": 37,
        }
    )


@dataclass
class FahrplanVerbindung(Strecke):
    """
    Eine Verbindungsanfrage beschreibt eine Kundenanfrage für eine Angebotsanfrage
    anhand Verbindungsinformationen aus dem Fahrplan.
    """
    verbindungs_segment: List[FahrplanVerbindungsSegment] = field(
        default_factory=list,
        metadata={
            "name": "verbindungsSegment",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    externe_verbindungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeVerbindungsReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class FreizeitBelegRequest(VertriebsRequest):
    leistung: List["FreizeitBelegRequest.Leistung"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    transaktions_verhalten: Optional[TransaktionsVerhalten] = field(
        default=None,
        metadata={
            "name": "transaktionsVerhalten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )

    @dataclass
    class Leistung:
        leistungs_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "leistungsId",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_inclusive": 0,
            }
        )
        beleg: List["FreizeitBelegRequest.Leistung.Beleg"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_occurs": 1,
            }
        )

        @dataclass
        class Beleg:
            beleg_parameter: List[FreizeitBelegParameter] = field(
                default_factory=list,
                metadata={
                    "name": "belegParameter",
                    "type": "Element",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                }
            )
            freizeit_traeger_medium_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "freizeitTraegerMediumCode",
                    "type": "Element",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                    "required": True,
                    "min_length": 0,
                    "max_length": 50,
                }
            )


@dataclass
class FreizeitBelegResponse(VertriebsResponse):
    """Die Belegantwort ist das Antwortsobjekt des 4.

    Klangs. Sie enthält für jede übermittelte LeistungId ein Objekt
    DruckDaten in dem alle zum Drucken notwendige Druckattribute
    enthalten sind.
    """
    leistung: List["FreizeitBelegResponse.Leistung"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class Leistung:
        leistungs_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "leistungsId",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_inclusive": 0,
            }
        )
        ausgabe_status: Optional[AusgabeStatusTyp] = field(
            default=None,
            metadata={
                "name": "ausgabeStatus",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
        beleg: List[FreizeitBeleg] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )


@dataclass
class LeistungEntsperrenRequest(VertriebsRequest):
    """
    Request-Element zum Entsperren einer Leistung.

    :ivar leistungs_id: ID der Leistung, welche entsperrt werden soll
    :ivar sperr_typ: Gibt an, ob die Leistung für Nutzung oder für
        Erstattung entsperrt werden soll
    :ivar begruendung: Begründung für die Entsperrung
    """
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    sperr_typ: Optional[SperrTyp] = field(
        default=None,
        metadata={
            "name": "sperrTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    begruendung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 4000,
        }
    )


@dataclass
class LeistungEntsperrenVertriebsResponse(VertriebsResponse):
    """
    Response-Element zum Entsperren einer Leistung.

    :ivar entsperrung_erfolgreich: Gibt an, ob die Entsperrung
        erfolgreich war
    """
    entsperrung_erfolgreich: Optional[bool] = field(
        default=None,
        metadata={
            "name": "entsperrungErfolgreich",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class LeistungSperrenRequest(VertriebsRequest):
    """
    Request-Element zum Sperren einer Leistung.

    :ivar leistungs_id: ID der Leistung, welche gesperrt werden soll
    :ivar gueltig_ab: Zeitpunkt ab wann die Leistung gesperrt werden
        soll
    :ivar gueltig_bis: Zeitpunkt bis wann die Leistung gesperrt werden
        soll. Leer = unbeschränkt
    :ivar begruendung: Begründung für die Sperrung
    :ivar sperr_typ: Gibt an, ob die Leistung für Nutzung oder für
        Erstattung gesperrt werden soll
    """
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    gueltig_ab: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigAb",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    gueltig_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    begruendung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 4000,
        }
    )
    sperr_typ: Optional[SperrTyp] = field(
        default=None,
        metadata={
            "name": "sperrTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class LeistungSperrenVertriebsResponse(VertriebsResponse):
    """
    Response-Element zum Sperren einer Leistung.

    :ivar sperrung_erfolgreich: Gibt an, ob die Sperrung erfolgreich war
    """
    sperrung_erfolgreich: Optional[bool] = field(
        default=None,
        metadata={
            "name": "sperrungErfolgreich",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class LeistungsAnrechnung:
    leistungs_info: Optional[LeistungsInfoType] = field(
        default=None,
        metadata={
            "name": "leistungsInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    angerechnete_zone: List[str] = field(
        default_factory=list,
        metadata={
            "name": "angerechneteZone",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class LeistungsKaufRequest:
    """
    Eine LeistungsKaufanfrage enthält alle Informationen, die notwendig sind, um
    die entsprechende Leistung kaufen zu können.
    """
    zahlungs_information: List[ZahlungsInformationRequest] = field(
        default_factory=list,
        metadata={
            "name": "zahlungsInformation",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    verkaufs_zeitpunkt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "verkaufsZeitpunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class LeistungsRequest:
    """
    Die Leistungsanfrage enthält alle Informationen, die notwendig sind, um für die
    übermittelte angebotsId eine Leistung offerieren zu können.

    :ivar verkaufs_parameter:
    :ivar angebots_id:
    :ivar externe_leistungs_referenz_id:
    :ivar externe_reisenden_referenz_id:
    :ivar leistungs_paket_id: Currently only implemented by NOVA FZ
        (Freizeit).
    :ivar angebots_paket_id: Currently only implemented by NOVA FZ
        (Freizeit).
    """
    verkaufs_parameter: List[LeistungVerkaufsParameterType] = field(
        default_factory=list,
        metadata={
            "name": "verkaufsParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    angebots_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "angebotsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "length": 37,
            "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    externe_leistungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeLeistungsReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
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
    leistungs_paket_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsPaketId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 1,
            "max_length": 37,
        }
    )
    angebots_paket_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "angebotsPaketId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class LeistungsStatusRequest(VertriebsRequest):
    """
    Über die Subklasse LeistungsstatusAnfrage wird die Anfrage für alle möglichen
    LeistungsStatus definiert.
    """
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )


@dataclass
class LeistungsStatusResponse(VertriebsResponse):
    """
    Die Spezialisierung LeistungsstatusAntwort dient als Container für alle
    ermittelten Leistungsstatus.
    """
    leistungs_status: Optional[LeistungsStatus] = field(
        default=None,
        metadata={
            "name": "leistungsStatus",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class LeistungsSuchRequest(VertriebsRequest):
    """
    Das Objekt LeistungsSuchanfrage dient als Container für notwendige
    Informationen zur LeistungsSuchanfrage.

    :ivar leistungs_schluessel: Suche über ein oder mehrere Leistungs-
        Fachschlüssel
    :ivar leistungs_feld: @Deprecated Will be removed in NOVA 15. Suche
        in einem oder mehreren Leistungs-Feldern. Werden mehrere Felder
        angegeben, so werden diese UND-verknüpft.
    :ivar leistung:
    :ivar paging_parameter: Durch das Hinzufügen der Paging-Parameter
        trefferOffset und maxTreffer können die Ergebnisse der
        LeistungsSuche paginiert werden.
    :ivar inklusive_kontroll_status: Legt fest, ob der Kontrollstatus
        der Leistung ermittelt werden soll. Dies ist nur für
        elektronisch kontrollierte Leistungen möglich. Nur true setzen,
        falls wirklich benötigt. Default=false
    :ivar inklusive_offeriert_leistungen:
    :ivar inklusive_begleitperson_leistungen:
    """
    leistungs_schluessel: List[LeistungsFachSchluessel] = field(
        default_factory=list,
        metadata={
            "name": "leistungsSchluessel",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    leistungs_feld: List[LeistungsSucheFeld] = field(
        default_factory=list,
        metadata={
            "name": "leistungsFeld",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    leistung: Optional["LeistungsSuchRequest.Leistung"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    paging_parameter: Optional[PagingParameter] = field(
        default=None,
        metadata={
            "name": "pagingParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    inklusive_kontroll_status: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inklusiveKontrollStatus",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    inklusive_offeriert_leistungen: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inklusiveOfferiertLeistungen",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    inklusive_begleitperson_leistungen: Optional[bool] = field(
        default=None,
        metadata={
            "name": "inklusiveBegleitpersonLeistungen",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class Leistung:
        """
        :ivar tkid:
        :ivar fahr_ausweis_art:
        :ivar traeger_medium_code:
        :ivar nutzungs_zeitraum: @Deprecated Will be removed in NOVA 15,
            please use gueltigkeitsZeitraum instead. / Schränkt die
            zurückgelieferten Leistungen auf diejenigen ein, deren
            Intervall [ersterNutzungsGeltungstag,
            letzterNutzungsGeltungstag] sich mit dem Intervall [von,
            bis] um mindestens 1 Tag überschneidet. Dieser Filter wird
            auf Leistungen, deren NutzungsInfo keinen
            erster/letzterNutzungsGeltungstag angibt, nicht angewendet
            (d.h. die Leistungen werden zurückgeliefert). UND-verknüpft
            mit erstellungszeitraum.
        :ivar gueltigkeits_zeitraum: Restricts the returned Leistungen
            to those whose intervals [ersterNutzungsGeltungstag,
            letzterNutzungsGeltungstag] and/or [entwertungsZeitraumVon,
            entwertungsZeitraumBis] overlap the given interval [von,
            bis]. AND-combined with erstellungszeitraum.
        :ivar erstellungs_zeitraum: Schränkt die zurückgelieferten
            Leistungen auf diejenigen ein, deren Erstellungszeitpunkt
            (Klang 2) sich mit dem Intervall [von, bis] überschneidet.
            UND-verknüpft mit nutzungsZeitraum.
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
        fahr_ausweis_art: Optional[FahrAusweisArt] = field(
            default=None,
            metadata={
                "name": "fahrAusweisArt",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        traeger_medium_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "traegerMediumCode",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_length": 0,
                "max_length": 50,
            }
        )
        nutzungs_zeitraum: Optional[DatumsZeitraum] = field(
            default=None,
            metadata={
                "name": "nutzungsZeitraum",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        gueltigkeits_zeitraum: Optional[Zeitraum] = field(
            default=None,
            metadata={
                "name": "gueltigkeitsZeitraum",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        erstellungs_zeitraum: Optional[Zeitraum] = field(
            default=None,
            metadata={
                "name": "erstellungsZeitraum",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )


@dataclass
class LeseFreizeitBelegStatusRequest(VertriebsRequest):
    leistung: List["LeseFreizeitBelegStatusRequest.Leistung"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Leistung:
        leistungs_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "leistungsId",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_inclusive": 0,
            }
        )
        traeger_medium_code: List[str] = field(
            default_factory=list,
            metadata={
                "name": "traegerMediumCode",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_length": 0,
                "max_length": 50,
            }
        )


@dataclass
class LeseFreizeitBelegStatusVertriebsResponse(VertriebsResponse):
    """Die Belegantwort ist das Antwortsobjekt des 4.

    Klangs. Sie enthält für jede übermittelte LeistungId ein Objekt
    DruckDaten in dem alle zum Drucken notwendige Druckattribute
    enthalten sind.
    """
    leistung: List["LeseFreizeitBelegStatusVertriebsResponse.Leistung"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class Leistung:
        leistungs_id: Optional[int] = field(
            default=None,
            metadata={
                "name": "leistungsId",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_inclusive": 0,
            }
        )
        traeger_medium_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "traegerMediumCode",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_length": 0,
                "max_length": 50,
            }
        )
        ausgabe_status: Optional[AusgabeStatusTyp] = field(
            default=None,
            metadata={
                "name": "ausgabeStatus",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
        beleg_parameter: List[FreizeitBelegParameter] = field(
            default_factory=list,
            metadata={
                "name": "belegParameter",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )


@dataclass
class ProduktEinflussFaktorGruppe:
    """
    ProdukteinflussfaktorGruppe beschreiben die unterschiedlichen Eigenschaften
    eines Angebots und dienen der flexiblen Bepreisung von Angeboten.
    """
    kunden_segment: Optional[KundenSegmentProduktEinflussFaktor] = field(
        default=None,
        metadata={
            "name": "kundenSegment",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    geltungs_dauer: Optional[GeltungsDauerProduktEinflussFaktor] = field(
        default=None,
        metadata={
            "name": "geltungsDauer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    generischer_einfluss_faktor: List[GenerischerProduktEinflussFaktor] = field(
        default_factory=list,
        metadata={
            "name": "generischerEinflussFaktor",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    traeger_medium: Optional[str] = field(
        default=None,
        metadata={
            "name": "traegerMedium",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    fahr_art: Optional[FahrArtTypCode] = field(
        default=None,
        metadata={
            "name": "fahrArt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    klasse: Optional[KlassenTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class ReiseGruppeInfo:
    preis_pro_reisender: Optional[Preis] = field(
        default=None,
        metadata={
            "name": "preisProReisender",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    kunden_segment: Optional[KundenSegmentProduktEinflussFaktor] = field(
        default=None,
        metadata={
            "name": "kundenSegment",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    anzahl: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 999,
        }
    )
    anzahl_gratis: Optional[int] = field(
        default=None,
        metadata={
            "name": "anzahlGratis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 999,
        }
    )


@dataclass
class ReisendenInfo:
    """
    Dieses Objekt enthält Informationen zum Reisenden, die einen Einfluss auf die
    Angebotsbestimmung haben.

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


@dataclass
class SavangebotsRequest(VertriebsRequest):
    """Die Klasse SAVAngebotsanfrage ist die abstrakte Basisklasse für alle
    Erneuerungs- und Erstattungs-Angebotsanfragen.

    Sie enthält die leistungsID oder die leistungsReferenz einer bereits
    verkauften und zu erstattenden oder zu erneuernden Leistung. Die
    SAVAngebotsanfrage ihrerseits ist eine Subklasse einer
    Vertriebsanfrage.
    """
    class Meta:
        name = "SAVAngebotsRequest"


@dataclass
class StornierungsRequest(VertriebsRequest):
    """
    Diese Klasse dient als Container für die zu stornierende Leistung.
    """
    leistungs_id: List[int] = field(
        default_factory=list,
        metadata={
            "name": "leistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
            "min_inclusive": 0,
        }
    )
    stornierungs_grund: Optional[str] = field(
        default=None,
        metadata={
            "name": "stornierungsGrund",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )


@dataclass
class StornierungsResponse(VertriebsResponse):
    stornierungs_info: List[StornierungsInfo] = field(
        default_factory=list,
        metadata={
            "name": "stornierungsInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class TarifWegKombinationsAngebotsRequest(VertriebsRequest):
    """Erzeugt ein streckenbasiertes Abo-Angebot dessen Geltungsbereich zwei
    unterschiedliche TarifWege abdeckt (Angebot mit zwei Strecken-Wegangaben).

    Tarifiert werden alle Wege aus den angefragten Angeboten.

    :ivar angebots_id: @Deprecated will be removed in NOVA 15. Beide
        Angebote müssen Abonnemente sein. Mind. 1 Angebot muss auf einem
        Produkt basieren das die Tarifierung mehrerer TarifWege erlaubt
        (Produktinfo.maxAnzahlTarifWege &gt; 1). Der Nutzungszeitraum
        der angefragten Angebote muss identisch sein. Jedes angefragte
        Angebot darf max. 1 TarifWeg abdecken.
    :ivar kombinierte_angebote:
    """
    angebots_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "angebotsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_occurs": 2,
            "length": 37,
            "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    kombinierte_angebote: List["TarifWegKombinationsAngebotsRequest.KombinierteAngebote"] = field(
        default_factory=list,
        metadata={
            "name": "kombinierteAngebote",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class KombinierteAngebote:
        angebots_id: List[str] = field(
            default_factory=list,
            metadata={
                "name": "angebotsId",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_occurs": 2,
                "max_occurs": 2,
                "length": 37,
                "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
            }
        )
        angebotskombination: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "min_length": 0,
                "max_length": 50,
            }
        )


@dataclass
class VerbindungTarifierbarkeitsResponse(VertriebsResponse):
    ist_tarifierbar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istTarifierbar",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    produkt_nummer: List[int] = field(
        default_factory=list,
        metadata={
            "name": "produktNummer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )


@dataclass
class VerkehrsKantenSequenz:
    """Die VerkehrskantenSequenz enthält eine Sequenz von Verkehrskanten.

    Die VerkehrskantenSequenz enthält alle Kanten des Wegs, die für das
    Angebot gefundenen wurden und VerkehrsMitteltyp fuer jede Kante.
    """
    kante: List[Kante] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    schnellste_reise_dauer: Optional[Dauer] = field(
        default=None,
        metadata={
            "name": "schnellsteReiseDauer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class VertragsBelegResponse(VertriebsResponse):
    vertrags_daten: List[VertragsDaten] = field(
        default_factory=list,
        metadata={
            "name": "vertragsDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class ZonenGeltungsBereich:
    zonen_buendel: List[ZonenBuendel] = field(
        default_factory=list,
        metadata={
            "name": "zonenBuendel",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    moegliche_zonen_buendel: List[ZonenBuendel] = field(
        default_factory=list,
        metadata={
            "name": "moeglicheZonenBuendel",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class AbstractLeistung:
    """
    Superklasse für Leistungen und SAVLeistungen.

    :ivar leistungs_typ:
    :ivar verkaufs_parameter:
    :ivar zahlungs_information:
    :ivar verkaufs_preis:
    :ivar tarif_stufe: Gesetzt bei Verbund-Fahrausweisen. i.d.R. 1
        Taristufe. Ausnahme: Bei gewissen Fahrausweisen die in Zonen
        unterschiedlicher Verbunde gültig sind wird pro Verbund eine
        eigene Tarifstufe ausgewiesen.
    :ivar rabatt_info:
    :ivar verkaeufer_information: Angaben zur Stelle, die diese Leistung
        verkauft hat.
    :ivar sav_protokoll: Liste aller SAV-Aktionen (Erstattungen,
        Annullationen), die für diese Leistung durchgeführt wurden.
    :ivar leistungs_id:
    :ivar erneuerungs_id: UUID der Leistung, die in der URL im
        ErneurungsInfoService verwendet wird
    :ivar leistungs_paket_id:
    :ivar externe_leistungs_referenz_id:
    :ivar leistungs_referenz:
    :ivar leistungs_status:
    :ivar offerte_gueltig_bis:
    :ivar externe_reisenden_referenz_id:
    :ivar verkaufs_zeitpunkt:
    :ivar erstellungs_zeitpunkt: Gibt an, wann diese Leistung in NOVAAN
        angelegt wurde (Klang 2).
    :ivar produkt_nummer:
    :ivar generation_stich_datum: Datum/Zeit des angewendeten
        Preisberechnungszeitpunkt und damit der DatenRelease-Zeitscheibe
        (Verkaufs- o. Reisezeitpunkt)
    :ivar daten_release_id:
    """
    leistungs_typ: Optional[LeistungsTyp] = field(
        default=None,
        metadata={
            "name": "leistungsTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    verkaufs_parameter: List[LeistungVerkaufsParameterType] = field(
        default_factory=list,
        metadata={
            "name": "verkaufsParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zahlungs_information: List[ZahlungsInformation] = field(
        default_factory=list,
        metadata={
            "name": "zahlungsInformation",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    verkaufs_preis: Optional[Preis] = field(
        default=None,
        metadata={
            "name": "verkaufsPreis",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    tarif_stufe: List[TarifStufe] = field(
        default_factory=list,
        metadata={
            "name": "tarifStufe",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    rabatt_info: List[RabattInfoType] = field(
        default_factory=list,
        metadata={
            "name": "rabattInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    verkaeufer_information: Optional[VerkaeuferInformation] = field(
        default=None,
        metadata={
            "name": "verkaeuferInformation",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    sav_protokoll: Optional["AbstractLeistung.SavProtokoll"] = field(
        default=None,
        metadata={
            "name": "savProtokoll",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    erneuerungs_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "erneuerungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    leistungs_paket_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsPaketId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 1,
            "max_length": 37,
        }
    )
    externe_leistungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeLeistungsReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    leistungs_referenz: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsReferenz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    leistungs_status: Optional[LeistungsStatus] = field(
        default=None,
        metadata={
            "name": "leistungsStatus",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    offerte_gueltig_bis: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "offerteGueltigBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
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
    verkaufs_zeitpunkt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "verkaufsZeitpunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    erstellungs_zeitpunkt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "erstellungsZeitpunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    generation_stich_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "generationStichDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    daten_release_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "datenReleaseId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 100,
        }
    )

    @dataclass
    class SavProtokoll:
        """
        :ivar sav_aktion: @Deprecated will be removed with NOVA 15.
            Please use savProtokollEintrag instead.
        :ivar sav_protokoll_eintrag:
        """
        sav_aktion: List[Savaktion] = field(
            default_factory=list,
            metadata={
                "name": "savAktion",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        sav_protokoll_eintrag: List[SavprotokollEintrag] = field(
            default_factory=list,
            metadata={
                "name": "savProtokollEintrag",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )


@dataclass
class AktivierungsAngebotsRequest(SavangebotsRequest):
    gueltig_ab: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigAb",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    gueltig_ab_zeitpunkt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "gueltigAbZeitpunkt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    abgangs_haltestelle: Optional[int] = field(
        default=None,
        metadata={
            "name": "abgangsHaltestelle",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )


@dataclass
class AngebotsKaufRequest(VertriebsRequest):
    leistungs_request: List[AngebotsKaufRequestParam] = field(
        default_factory=list,
        metadata={
            "name": "leistungsRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    transaktions_verhalten: Optional[TransaktionsVerhalten] = field(
        default=None,
        metadata={
            "name": "transaktionsVerhalten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class AngebotsRequest(VertriebsRequest):
    """Die Klasse AngebotsRequest ist die abstrakte Basisklasse für alle Strecken-,
    Zonen- und produktbasierten Angebotsanfragen.

    Die Angebotsanfrage ihrerseits ist eine Subklasse einer
    Vertriebsanfrage.

    :ivar traeger_medium:
    :ivar reisender:
    :ivar gruppen_reise_info:
    :ivar angebots_filter:
    :ivar klasse:
    :ivar rabatt_request:
    :ivar kunden_segmente_gruppieren: Wenn true, werden falls moeglich
        Angebote fuer eine KundenSegmentgruppe (z.B. ERMAESSIGT) statt
        Einzel-KundenSegmente (z.B. KIND_6-16, HALBTAX etc.) geliefert.
        Insbesondere bei Angebotsanfragen ohne ReisendenInfo wird
        dadurch die Angebotsmenge stark reduziert.
    :ivar vertrags_partner:
    :ivar basis_vertrags_nummer:
    """
    traeger_medium: List[str] = field(
        default_factory=list,
        metadata={
            "name": "traegerMedium",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    reisender: List[ReisendenInfo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    gruppen_reise_info: List[GruppenReiseInfoRequest] = field(
        default_factory=list,
        metadata={
            "name": "gruppenReiseInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    angebots_filter: List[AngebotsFilter] = field(
        default_factory=list,
        metadata={
            "name": "angebotsFilter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    klasse: List[KlassenTypCode] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    rabatt_request: Optional[RabattAnfrageType] = field(
        default=None,
        metadata={
            "name": "rabattRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    kunden_segmente_gruppieren: Optional[bool] = field(
        default=None,
        metadata={
            "name": "kundenSegmenteGruppieren",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    vertrags_partner: Optional[str] = field(
        default=None,
        metadata={
            "name": "vertragsPartner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    basis_vertrags_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "basisVertragsNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 10,
        }
    )


@dataclass
class EntschaedigungsAngebotsRequest(SavangebotsRequest):
    """Eine EntschädigungsAngebotsanfrage ist eine spezielle Art einer
    SAVAngebotsanfrage.

    Sie wird verwendet, wenn eine bereits verkaufte Leistung bei
    Verspätungen im öV entschädigt werden soll. Siehe auch
    SAVAngebotsAnfrage.
    """
    zu_entschaedigende_leistung: List[int] = field(
        default_factory=list,
        metadata={
            "name": "zuEntschaedigendeLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
            "min_inclusive": 0,
        }
    )
    verspaetungs_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "verspaetungsDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    verspaetung_in_minuten: Optional[int] = field(
        default=None,
        metadata={
            "name": "verspaetungInMinuten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 9999,
        }
    )
    min_entschaedigungs_betrag_anwenden: Optional[bool] = field(
        default=None,
        metadata={
            "name": "minEntschaedigungsBetragAnwenden",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class ErneuerungsAngebotsRequest(SavangebotsRequest):
    """Die ErneuerungsAngebotsanfrage ist eine spezielle Art einer
    SAVAngebotsanfrage.

    Ihr wird nebst der leistungsID oder leistungsReferenz ein gültigAb
    Datum mitgegeben, ab wann die zu erneuernde Leistung gültig sein
    soll. Im Falle von personalisierten Angeboten enthält sie zudem
    einen Reisenden. Siehe auch SAVAngebotsAnfrage.
    """
    erneuerungs_request: List[ErneuerungsRequest] = field(
        default_factory=list,
        metadata={
            "name": "erneuerungsRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )


@dataclass
class ErstattungsAngebotsRequest(SavangebotsRequest):
    """Eine ErstattungsAngebotsanfrage ist eine spezielle Art einer
    SAVAngebotsanfrage.

    Sie wird verwendet, wenn eine bereits verkaufte Leistung erstattet
    werden soll. Siehe auch SAVAngebotsAnfrage.

    :ivar selbst_behalt:
    :ivar zu_erstattende_leistung:
    :ivar selbst_behalt_empfaenger: Partner-Code des Selbstbehalt-
        Empfänger (sofern abweichend von Vermittler)
    """
    selbst_behalt: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "selbstBehalt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zu_erstattende_leistung: List[LeistungErstattungsRequest] = field(
        default_factory=list,
        metadata={
            "name": "zuErstattendeLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    selbst_behalt_empfaenger: Optional[int] = field(
        default=None,
        metadata={
            "name": "selbstBehaltEmpfaenger",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 99999,
        }
    )


@dataclass
class HinterlegungsAngebotsRequest(SavangebotsRequest):
    vertrags_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "vertragsNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 10,
        }
    )
    hinterlegung_von: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "hinterlegungVon",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    hinterlegung_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "hinterlegungBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class KaufRequest(VertriebsRequest):
    """
    Das Objekt Kaufanfrage dient als Container für mehrere LeistungsKaufanfragen.
    """
    leistungs_kauf_request: List[LeistungsKaufRequest] = field(
        default_factory=list,
        metadata={
            "name": "leistungsKaufRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    transaktions_verhalten: Optional[TransaktionsVerhalten] = field(
        default=None,
        metadata={
            "name": "transaktionsVerhalten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class NutzungsInfo:
    """
    Liefert Informationen zur Nutzung eines Angebots wie Geltungstage und -zeiten.

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


@dataclass
class OevAnfrageParameterType:
    fahrt_wunsch: Optional["OevAnfrageParameterType.FahrtWunsch"] = field(
        default=None,
        metadata={
            "name": "fahrtWunsch",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    reisender: List["OevAnfrageParameterType.Reisender"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    angebots_filter: List[AngebotsFilter] = field(
        default_factory=list,
        metadata={
            "name": "angebotsFilter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    traeger_medium: List[str] = field(
        default_factory=list,
        metadata={
            "name": "traegerMedium",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    gewuenschte_klasse: List[KlassenTypCode] = field(
        default_factory=list,
        metadata={
            "name": "gewuenschteKlasse",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class FahrtWunsch:
        hin_fahrt_verbindung: Optional[FahrplanVerbindung] = field(
            default=None,
            metadata={
                "name": "hinFahrtVerbindung",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
        rueck_fahrt_verbindung: Optional[FahrplanVerbindung] = field(
            default=None,
            metadata={
                "name": "rueckFahrtVerbindung",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        datum_rueck_fahrt: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "datumRueckFahrt",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        zeitpunkt_rueck_fahrt: Optional[XmlTime] = field(
            default=None,
            metadata={
                "name": "zeitpunktRueckFahrt",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )

    @dataclass
    class Reisender(ReisendenInfo):
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )


@dataclass
class OffertenRequest(VertriebsRequest):
    """
    Das Objekt Offertenanfrage dient als Container für mehrere Leistungsanfragen.
    """
    leistungs_request: List[LeistungsRequest] = field(
        default_factory=list,
        metadata={
            "name": "leistungsRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    transaktions_verhalten: Optional[TransaktionsVerhalten] = field(
        default=None,
        metadata={
            "name": "transaktionsVerhalten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class TeilStrecke:
    teil_strecke: Optional[VerkehrsKantenSequenz] = field(
        default=None,
        metadata={
            "name": "teilStrecke",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    weg_position: Optional[WegPosition] = field(
        default=None,
        metadata={
            "name": "wegPosition",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class VerbindungTarifierbarkeitsRequest(VertriebsRequest):
    verbindung: Optional[FahrplanVerbindung] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class BestaetigeProduktion:
    """
    Request-Element für die abschliessende Bestätigung der Produktion.
    """
    class Meta:
        name = "bestaetigeProduktion"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    bestaetige_produktion_request: Optional[BestaetigeProduktionRequest] = field(
        default=None,
        metadata={
            "name": "bestaetigeProduktionRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ErstelleBelege:
    """Request-Element für den 4.

    Klang
    """
    class Meta:
        name = "erstelleBelege"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    beleg_request: Optional[BelegRequest] = field(
        default=None,
        metadata={
            "name": "belegRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ErstelleFreizeitBelege:
    class Meta:
        name = "erstelleFreizeitBelege"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    freizeit_beleg_request: Optional[FreizeitBelegRequest] = field(
        default=None,
        metadata={
            "name": "freizeitBelegRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ErstelleFreizeitBelegeResponse:
    class Meta:
        name = "erstelleFreizeitBelegeResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    freizeit_beleg_response: Optional[FreizeitBelegResponse] = field(
        default=None,
        metadata={
            "name": "freizeitBelegResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ErstelleSavangebote:
    """Request-Element für den 1.

    Klang (SAV)
    """
    class Meta:
        name = "erstelleSAVAngebote"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    sav_request: Optional[SavangebotsRequest] = field(
        default=None,
        metadata={
            "name": "savRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ErstelleTarifWegKombinationsAngebot:
    class Meta:
        name = "erstelleTarifWegKombinationsAngebot"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_request: Optional[TarifWegKombinationsAngebotsRequest] = field(
        default=None,
        metadata={
            "name": "angebotsRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ErstelleVertragsBelege:
    class Meta:
        name = "erstelleVertragsBelege"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    vertrags_beleg_request: Optional[BelegRequest] = field(
        default=None,
        metadata={
            "name": "vertragsBelegRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ErstelleVertragsBelegeResponse:
    class Meta:
        name = "erstelleVertragsBelegeResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    vertrags_beleg_response: Optional[VertragsBelegResponse] = field(
        default=None,
        metadata={
            "name": "vertragsBelegResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetLeistungsStatus:
    class Meta:
        name = "getLeistungsStatus"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistungs_status_request: Optional[LeistungsStatusRequest] = field(
        default=None,
        metadata={
            "name": "leistungsStatusRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GetLeistungsStatusResponse:
    class Meta:
        name = "getLeistungsStatusResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistungs_status_response: Optional[LeistungsStatusResponse] = field(
        default=None,
        metadata={
            "name": "leistungsStatusResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LeistungEntsperren:
    class Meta:
        name = "leistungEntsperren"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistung_entsperren_request: Optional[LeistungEntsperrenRequest] = field(
        default=None,
        metadata={
            "name": "leistungEntsperrenRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LeistungEntsperrenResponse:
    class Meta:
        name = "leistungEntsperrenResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistung_entsperren_response: Optional[LeistungEntsperrenVertriebsResponse] = field(
        default=None,
        metadata={
            "name": "leistungEntsperrenResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LeistungSperren:
    class Meta:
        name = "leistungSperren"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistung_sperren_request: Optional[LeistungSperrenRequest] = field(
        default=None,
        metadata={
            "name": "leistungSperrenRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LeistungSperrenResponse:
    class Meta:
        name = "leistungSperrenResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistung_sperren_response: Optional[LeistungSperrenVertriebsResponse] = field(
        default=None,
        metadata={
            "name": "leistungSperrenResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LeseFreizeitBelegStatus:
    class Meta:
        name = "leseFreizeitBelegStatus"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    lese_freizeit_beleg_status_request: Optional[LeseFreizeitBelegStatusRequest] = field(
        default=None,
        metadata={
            "name": "leseFreizeitBelegStatusRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LeseFreizeitBelegStatusResponse:
    class Meta:
        name = "leseFreizeitBelegStatusResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    lese_freizeit_beleg_status_response: Optional[LeseFreizeitBelegStatusVertriebsResponse] = field(
        default=None,
        metadata={
            "name": "leseFreizeitBelegStatusResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LiefereBelegeFuerAngebot:
    """
    Request-Element für die Beleganfrage auf Basis einer AngebotsId.
    """
    class Meta:
        name = "liefereBelegeFuerAngebot"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_beleg_request: Optional[AngebotsBelegRequest] = field(
        default=None,
        metadata={
            "name": "angebotsBelegRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LiefereBelegeFuerAngebotResponse:
    """
    Response-Element für die Beleganfrage auf Basis einer AngebotsId.
    """
    class Meta:
        name = "liefereBelegeFuerAngebotResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_beleg_response: Optional[AngebotsBelegResponse] = field(
        default=None,
        metadata={
            "name": "angebotsBelegResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PruefenVerbindungTarifierbarkeitsResponse:
    class Meta:
        name = "pruefenVerbindungTarifierbarkeitsResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    verbindung_tarifierbarkeits_response: Optional[VerbindungTarifierbarkeitsResponse] = field(
        default=None,
        metadata={
            "name": "verbindungTarifierbarkeitsResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class StorniereLeistung:
    class Meta:
        name = "storniereLeistung"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    stornierungs_request: Optional[StornierungsRequest] = field(
        default=None,
        metadata={
            "name": "stornierungsRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class StorniereLeistungResponse:
    class Meta:
        name = "storniereLeistungResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    stornierungs_response: Optional[StornierungsResponse] = field(
        default=None,
        metadata={
            "name": "stornierungsResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SucheLeistungen:
    class Meta:
        name = "sucheLeistungen"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistungs_such_request: Optional[LeistungsSuchRequest] = field(
        default=None,
        metadata={
            "name": "leistungsSuchRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Angebot(AbstractAngebot):
    """
    Die Klasse repräsentiert ein Angebot, das von der öV-Plattform für eine
    Angebotsanfrage erzeugt wurde.
    """
    nutzungs_info: Optional[NutzungsInfo] = field(
        default=None,
        metadata={
            "name": "nutzungsInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    zuschlags_angebot_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "zuschlagsAngebotRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "tokens": True,
        }
    )
    produkt_einfluss_faktoren: Optional[ProduktEinflussFaktorGruppe] = field(
        default=None,
        metadata={
            "name": "produktEinflussFaktoren",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    geltungs_bereich_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "geltungsBereichRef",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    bewertungs_info: Optional[AngebotBewertungsInfo] = field(
        default=None,
        metadata={
            "name": "bewertungsInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    reise_gruppen_info: List[ReiseGruppeInfo] = field(
        default_factory=list,
        metadata={
            "name": "reiseGruppenInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    vertrags_info: Optional[VertragsInfo] = field(
        default=None,
        metadata={
            "name": "vertragsInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    bestehende_leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "bestehendeLeistungsId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    externe_leistungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeLeistungsReferenzId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    fahrt_wunsch_abdeckung: Optional[FahrtWunschAbdeckung] = field(
        default=None,
        metadata={
            "name": "fahrtWunschAbdeckung",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    fq_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "fqCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    nachtraegliche_einlieferung_moeglich: Optional[bool] = field(
        default=None,
        metadata={
            "name": "nachtraeglicheEinlieferungMoeglich",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    enthaelt_swiss_pass_karte: bool = field(
        default=False,
        metadata={
            "name": "enthaeltSwissPassKarte",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    benoetigt_neues_foto: bool = field(
        default=False,
        metadata={
            "name": "benoetigtNeuesFoto",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    kauf_erforderlich: Optional[bool] = field(
        default=None,
        metadata={
            "name": "kaufErforderlich",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class AngebotsKaufResponse(VertriebsResponse):
    """
    :ivar leistung:
    :ivar fehler: Im Falle von Fehlern bei der Verarbeitung einzelner
        Leistungen werden hier die leistungsbezogenen Fehlermeldungen
        zurückgeliefert. Allgemeine Fehlermeldungen werden auf Top-
        Level-Ebene der AngebotsKaufantwort zurückgeliefert.
    """
    leistung: List[AbstractLeistung] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    fehler: List["AngebotsKaufResponse.Fehler"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class Fehler:
        meldungen: Optional[Meldungen] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
        angebots_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "angebotsId",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "length": 37,
                "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
            }
        )
        externe_leistungs_referenz_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "externeLeistungsReferenzId",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_length": 0,
                "max_length": 50,
            }
        )


@dataclass
class BestaetigeProduktionVertriebsResponse(VertriebsResponse):
    """
    Diese Klasse dient als Container für alle Leistungen, deren Produktion
    bestätigt worden ist.
    """
    leistung: List[AbstractLeistung] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class FreizeitKombinationAngebotsRequest(VertriebsRequest):
    oev_anfrage_parameter: Optional[OevAnfrageParameterType] = field(
        default=None,
        metadata={
            "name": "oevAnfrageParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    freizeit_angebot: List["FreizeitKombinationAngebotsRequest.FreizeitAngebot"] = field(
        default_factory=list,
        metadata={
            "name": "freizeitAngebot",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    transaktions_verhalten: Optional[TransaktionsVerhalten] = field(
        default=None,
        metadata={
            "name": "transaktionsVerhalten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )

    @dataclass
    class FreizeitAngebot:
        freizeit_angebots_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "freizeitAngebotsId",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "length": 37,
                "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
            }
        )
        oev_reisender_ref: Optional[str] = field(
            default=None,
            metadata={
                "name": "oevReisenderRef",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )


@dataclass
class KaufResponse(VertriebsResponse):
    """Die Kaufantwort ist das Antwortsobjekt des 3.

    Klangs. Sie enthält für jede übermittelte LeistungId eine Leistung
    mit dem Status gekauft.
    """
    leistung: List[AbstractLeistung] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class LeistungsDruckDaten:
    leistung: Optional[AbstractLeistung] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    beleg: List[DruckBeleg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class LeistungsSuchErgebnis:
    """
    :ivar leistung:
    :ivar kontroll_status: Nur gefüllt, wenn in der Suche explizit
        angefragt.
    :ivar lv_notiz: Optionale Notiz zu einer Leistung. Kann durch
        Support (z.B. Leitstelle, Vertrieb) gesetzt werden.
    """
    leistung: Optional[AbstractLeistung] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    kontroll_status: List[KontrollStatus] = field(
        default_factory=list,
        metadata={
            "name": "kontrollStatus",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    lv_notiz: Optional[str] = field(
        default=None,
        metadata={
            "name": "lvNotiz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 4000,
        }
    )


@dataclass
class OffertenResponse(VertriebsResponse):
    """Die Offertenantwort ist das Antwortobjekt des 2.

    Klangs. Sie enthält für jede übermittelte angebotsId eine offerierte
    Leistung.
    """
    leistung: List[AbstractLeistung] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class ProduktBasierterAngebotsRequest(AngebotsRequest):
    """
    :ivar freie_preis_eingabe:
    :ivar mindest_vertrags_dauer:
    :ivar parkplatz:
    :ivar gueltig_ab_datum:
    :ivar gueltig_ab_zeit:
    :ivar standort: @Deprecated Will be removed in NOVA 15. Replaced by
        parkplatz.
    :ivar bestehende_vertrags_nummer:
    :ivar ist_neuer_vertrag:
    :ivar provision_lv: Temporär benötigtes Attribut wird nur für
        interne Zwecke genutzt.
    """
    freie_preis_eingabe: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "freiePreisEingabe",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    mindest_vertrags_dauer: Optional[Dauer] = field(
        default=None,
        metadata={
            "name": "mindestVertragsDauer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    parkplatz: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 9999999,
        }
    )
    gueltig_ab_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigAbDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    gueltig_ab_zeit: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "gueltigAbZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    standort: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 99999,
        }
    )
    bestehende_vertrags_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "bestehendeVertragsNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 10,
        }
    )
    ist_neuer_vertrag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istNeuerVertrag",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    provision_lv: Optional[int] = field(
        default=None,
        metadata={
            "name": "provisionLV",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 99999,
        }
    )


@dataclass
class Savleistung(AbstractLeistung):
    """
    :ivar total_erstattungs_betraege:
    :ivar erstattete_leistung:
    :ivar erstattungs_begruendung:
    :ivar selbst_behalt:
    :ivar traeger_medium: Momentan konstant "SICHERHEITSPAPIER"
    """
    class Meta:
        name = "SAVLeistung"

    total_erstattungs_betraege: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "totalErstattungsBetraege",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    erstattete_leistung: List[ErstatteteLeistung] = field(
        default_factory=list,
        metadata={
            "name": "erstatteteLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    erstattungs_begruendung: Optional[str] = field(
        default=None,
        metadata={
            "name": "erstattungsBegruendung",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 200,
        }
    )
    selbst_behalt: Optional[str] = field(
        default=None,
        metadata={
            "name": "selbstBehalt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "total_digits": 12,
            "fraction_digits": 2,
            "pattern": r"-?[0-9]{1,10}(\.[0-9]{0,2})?",
        }
    )
    traeger_medium: Optional[str] = field(
        default=None,
        metadata={
            "name": "traegerMedium",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class StreckenBasierterAngebotsRequest(AngebotsRequest):
    """Die Klasse repräsentiert streckenbasierte Angebotsanfragen.

    Streckenbasierte Angebotsanfragen beschreiben den Reisewunsch eines
    Kunden.
    """
    weg_suche: Optional[WegSuche] = field(
        default=None,
        metadata={
            "name": "wegSuche",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    hin_fahrt_verbindung: Optional[FahrplanVerbindung] = field(
        default=None,
        metadata={
            "name": "hinFahrtVerbindung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    rueck_fahrt: Optional["StreckenBasierterAngebotsRequest.RueckFahrt"] = field(
        default=None,
        metadata={
            "name": "rueckFahrt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zonen_buendel_request: List[ZonenBuendelRequest] = field(
        default_factory=list,
        metadata={
            "name": "zonenBuendelRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class RueckFahrt:
        """
        :ivar verbindung:
        :ivar zeit_angabe:
        :ivar retour_angebote_zusaetzlich_anbieten: Diese Option
            erstellt keine zusätzlichen Angebote und berücksichtigt
            keine Rückwege, sondern dient zur intelligenteren Filterung
            von Angeboten, die nur auf der Basis von einem
            HinfahrtVerbindung erstellt werden. Retour-Angebote, deren
            NutzungsGeltungsdauer nicht 2x Zeit der Verbindung +
            Pufferzeit für einen potentiellen Aufenthaltsdauer abdeckt,
            werden herausgefiltert.
        """
        verbindung: Optional[FahrplanVerbindung] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        zeit_angabe: Optional["StreckenBasierterAngebotsRequest.RueckFahrt.ZeitAngabe"] = field(
            default=None,
            metadata={
                "name": "zeitAngabe",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        retour_angebote_zusaetzlich_anbieten: Optional["StreckenBasierterAngebotsRequest.RueckFahrt.RetourAngeboteZusaetzlichAnbieten"] = field(
            default=None,
            metadata={
                "name": "retourAngeboteZusaetzlichAnbieten",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )

        @dataclass
        class ZeitAngabe:
            """
            :ivar datum_rueck_fahrt: Datum der Rückfahrt für
                FahrplanVerbindungsanfragen ohne Angabe einer
                Rückfahrtverbindung und für Weganfragen.
            :ivar zeitpunkt_rueck_fahrt: Zeitpunkt der Rückfahrt für
                FahrplanVerbindungsanfragen ohne Angabe einer
                Rückfahrtverbindung und für Weganfragen.
            """
            datum_rueck_fahrt: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "name": "datumRueckFahrt",
                    "type": "Attribute",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                }
            )
            zeitpunkt_rueck_fahrt: Optional[XmlTime] = field(
                default=None,
                metadata={
                    "name": "zeitpunktRueckFahrt",
                    "type": "Attribute",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                }
            )

        @dataclass
        class RetourAngeboteZusaetzlichAnbieten:
            """
            :ivar value:
            :ivar pufferzeit_aufenthaltsdauer_minuten: Nova-Benutzer
                können den Wert der Pufferzeit (in Minuten) einstellen,
                um die Filterung von Retourenangeboten anzupassen (falls
                leer, wird der Defaultwert (180 Minuten) angewendet.).
            """
            value: Optional[bool] = field(
                default=None,
                metadata={
                    "required": True,
                }
            )
            pufferzeit_aufenthaltsdauer_minuten: Optional[int] = field(
                default=None,
                metadata={
                    "name": "pufferzeitAufenthaltsdauerMinuten",
                    "type": "Attribute",
                    "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                    "max_inclusive": 9999,
                }
            )


@dataclass
class StreckenWechselAngebotsRequest(AngebotsRequest):
    bestehender_weg: Optional[WegSuche] = field(
        default=None,
        metadata={
            "name": "bestehenderWeg",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    strecke: Optional[Strecke] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    bestehende_klasse: Optional[KlassenTypCode] = field(
        default=None,
        metadata={
            "name": "bestehendeKlasse",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class VerkehrsStrecke:
    """
    :ivar tarifierte_strecke:
    :ivar nicht_tarifierte_teil_strecke: Am Weganfang oder Wegende
        entfernte Teilstrecken, die nicht tarifiert wurden.
    :ivar id:
    :ivar externe_verbindungs_referenz_id: externeVerbindungsReferenzId
        werden nur für Angebote geliefert.
    """
    tarifierte_strecke: Optional[VerkehrsKantenSequenz] = field(
        default=None,
        metadata={
            "name": "tarifierteStrecke",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    nicht_tarifierte_teil_strecke: List[TeilStrecke] = field(
        default_factory=list,
        metadata={
            "name": "nichtTarifierteTeilStrecke",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    externe_verbindungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeVerbindungsReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class ZonenplanBasierterAngebotsRequest(AngebotsRequest):
    abgangs_haltestelle: Optional[int] = field(
        default=None,
        metadata={
            "name": "abgangsHaltestelle",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    verbund_strecken_request: Optional[VerbundStreckenRequest] = field(
        default=None,
        metadata={
            "name": "verbundStreckenRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zonen_request: Optional[ZonenRequest] = field(
        default=None,
        metadata={
            "name": "zonenRequest",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    freie_preis_eingabe: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "freiePreisEingabe",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    gueltig_ab_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigAbDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    gueltig_ab_zeit: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "gueltigAbZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class ZuErstattendeLeistung:
    original_leistung: Optional[AbstractLeistung] = field(
        default=None,
        metadata={
            "name": "originalLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    erstattungs_daten: Optional[ErstattungsDaten] = field(
        default=None,
        metadata={
            "name": "erstattungsDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class ErstelleAngebote:
    """Request-Element für den 1.

    Klang
    """
    class Meta:
        name = "erstelleAngebote"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_request: Optional[AngebotsRequest] = field(
        default=None,
        metadata={
            "name": "angebotsRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class KaufeAngebote:
    """
    Request-Element für den nachgelagerten Verkauf.
    """
    class Meta:
        name = "kaufeAngebote"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_kauf_request: Optional[AngebotsKaufRequest] = field(
        default=None,
        metadata={
            "name": "angebotsKaufRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class KaufeLeistungen:
    """Request-Element für den 3.

    Klang
    """
    class Meta:
        name = "kaufeLeistungen"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    kauf_request: Optional[KaufRequest] = field(
        default=None,
        metadata={
            "name": "kaufRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OfferiereLeistungen:
    """Request-Element für den 2.

    Klang
    """
    class Meta:
        name = "offeriereLeistungen"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    offerten_request: Optional[OffertenRequest] = field(
        default=None,
        metadata={
            "name": "offertenRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PruefenVerbindungTarifierbarkeits:
    class Meta:
        name = "pruefenVerbindungTarifierbarkeits"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    verbindung_tarifierbarkeits_request: Optional[VerbindungTarifierbarkeitsRequest] = field(
        default=None,
        metadata={
            "name": "verbindungTarifierbarkeitsRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class BelegResponse(VertriebsResponse):
    """Die Belegantwort ist das Antwortsobjekt des 4.

    Klangs. Sie enthält für jede übermittelte LeistungId ein Objekt
    DruckDaten in dem alle zum Drucken notwendige Druckattribute
    enthalten sind.
    """
    leistungs_druck_daten: List[LeistungsDruckDaten] = field(
        default_factory=list,
        metadata={
            "name": "leistungsDruckDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class LeistungsSuchResponse(VertriebsResponse):
    """
    Die LeistungsSuchantwort liefert eine Auflistung von Leistungen.
    """
    leistungs_such_ergebnis: List[LeistungsSuchErgebnis] = field(
        default_factory=list,
        metadata={
            "name": "leistungsSuchErgebnis",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    ist_teil_ergebnis: Optional[bool] = field(
        default=None,
        metadata={
            "name": "istTeilErgebnis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class Savangebot(AbstractAngebot):
    """
    Angebot für SAV (Erneuerung, Erstattung), die über SAVAngebotsanfrage
    angefordert wurde.

    :ivar zu_erstattende_leistung:
    :ivar total_erstattungs_betraege:
    :ivar max_selbstbehalt:
    :ivar angewendeter_selbstbehalt:
    :ivar min_selbstbehalt:
    :ivar ausweis_pflicht:
    :ivar traeger_medium: Aktuell konstant "SICHERHEITSPAPIER"
    """
    class Meta:
        name = "SAVAngebot"

    zu_erstattende_leistung: List[ZuErstattendeLeistung] = field(
        default_factory=list,
        metadata={
            "name": "zuErstattendeLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    total_erstattungs_betraege: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "totalErstattungsBetraege",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    max_selbstbehalt: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "maxSelbstbehalt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    angewendeter_selbstbehalt: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "angewendeterSelbstbehalt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    min_selbstbehalt: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "minSelbstbehalt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    ausweis_pflicht: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ausweisPflicht",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    traeger_medium: Optional[str] = field(
        default=None,
        metadata={
            "name": "traegerMedium",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )


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


@dataclass
class BestaetigeProduktionResponse:
    """
    Response-Element für die abschliessende Bestätigung der Produktion.
    """
    class Meta:
        name = "bestaetigeProduktionResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    bestaetige_produktion_response: Optional[BestaetigeProduktionVertriebsResponse] = field(
        default=None,
        metadata={
            "name": "bestaetigeProduktionResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ErstelleFreizeitKombiAngebot:
    class Meta:
        name = "erstelleFreizeitKombiAngebot"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_request: Optional[FreizeitKombinationAngebotsRequest] = field(
        default=None,
        metadata={
            "name": "angebotsRequest",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class KaufeAngeboteResponse:
    """
    Response-Element für den nachgelagerten Verkauf.
    """
    class Meta:
        name = "kaufeAngeboteResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_kauf_response: Optional[AngebotsKaufResponse] = field(
        default=None,
        metadata={
            "name": "angebotsKaufResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class KaufeLeistungenResponse:
    """Response-Element für den 3.

    Klang
    """
    class Meta:
        name = "kaufeLeistungenResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    kauf_response: Optional[KaufResponse] = field(
        default=None,
        metadata={
            "name": "kaufResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OfferiereLeistungenResponse:
    """Response-Element für den 2.

    Klang
    """
    class Meta:
        name = "offeriereLeistungenResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    offerten_response: Optional[OffertenResponse] = field(
        default=None,
        metadata={
            "name": "offertenResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class GeltungsBereich:
    weg_angabe: List[WegAngabe] = field(
        default_factory=list,
        metadata={
            "name": "wegAngabe",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    meldungen_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "meldungenRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "tokens": True,
        }
    )
    zonen_geltungs_bereich: Optional[ZonenGeltungsBereich] = field(
        default=None,
        metadata={
            "name": "zonenGeltungsBereich",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    strecken_geltungs_bereich: Optional[StreckenGeltungsBereich] = field(
        default=None,
        metadata={
            "name": "streckenGeltungsBereich",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    parkplatz: Optional[Parkplatz] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )


@dataclass
class ErstelleBelegeResponse:
    """Response-Element für den 4.

    Klang
    """
    class Meta:
        name = "erstelleBelegeResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    beleg_response: Optional[BelegResponse] = field(
        default=None,
        metadata={
            "name": "belegResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SucheLeistungenResponse:
    class Meta:
        name = "sucheLeistungenResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    leistungs_such_response: Optional[LeistungsSuchResponse] = field(
        default=None,
        metadata={
            "name": "leistungsSuchResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AngebotsResponse(VertriebsResponse):
    """
    Die Klasse Angebotsantwort dient als Container für die ermittelten Angebote und
    beinhaltet zusätzlich angebotsübergreifende Informationen.
    """
    angebote: Optional["AngebotsResponse.Angebote"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    reisende: Optional["AngebotsResponse.Reisende"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    angebots_pakete: Optional["AngebotsResponse.AngebotsPakete"] = field(
        default=None,
        metadata={
            "name": "angebotsPakete",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    geltungs_bereiche: Optional["AngebotsResponse.GeltungsBereiche"] = field(
        default=None,
        metadata={
            "name": "geltungsBereiche",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )

    @dataclass
    class Angebote:
        """
        :ivar angebot: Abhängig von der Anfrage (Angebotsanfrage,
            SAVAngebotsanfrage) sind hier Instanzen von Angebot oder
            SAVAngebot enthalten.
        """
        angebot: List[AbstractAngebot] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )

    @dataclass
    class Reisende:
        reisender: List[Reisender] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )

    @dataclass
    class AngebotsPakete:
        angebots_paket: List[AngebotsPaket] = field(
            default_factory=list,
            metadata={
                "name": "angebotsPaket",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )

    @dataclass
    class GeltungsBereiche:
        geltungs_bereich: List[GeltungsBereich] = field(
            default_factory=list,
            metadata={
                "name": "geltungsBereich",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )


@dataclass
class Leistung(AbstractLeistung):
    """Eine Leistung entsteht aus einem angebotenen Angebot.

    Eine Leistung wird in der Regel offeriert, Verkauft und
    anschliessend produziert.

    :ivar nutzungs_info:
    :ivar aktivierte_leistung:
    :ivar produkt_einfluss_faktoren:
    :ivar geltungs_bereich:
    :ivar reise_gruppen_info:
    :ivar vertrags_info: Information zum Vertrag in SAV
    :ivar enthaelt_swiss_pass_karte:
    :ivar benoetigt_neues_foto:
    """
    nutzungs_info: Optional[NutzungsInfo] = field(
        default=None,
        metadata={
            "name": "nutzungsInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    aktivierte_leistung: List["Leistung"] = field(
        default_factory=list,
        metadata={
            "name": "aktivierteLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    produkt_einfluss_faktoren: Optional[ProduktEinflussFaktorGruppe] = field(
        default=None,
        metadata={
            "name": "produktEinflussFaktoren",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    geltungs_bereich: Optional[GeltungsBereich] = field(
        default=None,
        metadata={
            "name": "geltungsBereich",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    reise_gruppen_info: List[ReiseGruppeInfo] = field(
        default_factory=list,
        metadata={
            "name": "reiseGruppenInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    vertrags_info: Optional[VertragsInfo] = field(
        default=None,
        metadata={
            "name": "vertragsInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    enthaelt_swiss_pass_karte: bool = field(
        default=False,
        metadata={
            "name": "enthaeltSwissPassKarte",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    benoetigt_neues_foto: bool = field(
        default=False,
        metadata={
            "name": "benoetigtNeuesFoto",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )


@dataclass
class ErstelleAngeboteResponse:
    """Response-Element für den 1.

    Klang
    """
    class Meta:
        name = "erstelleAngeboteResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_response: Optional[AngebotsResponse] = field(
        default=None,
        metadata={
            "name": "angebotsResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ErstelleFreizeitKombiAngebotResponse:
    class Meta:
        name = "erstelleFreizeitKombiAngebotResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_response: Optional[AngebotsResponse] = field(
        default=None,
        metadata={
            "name": "angebotsResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ErstelleSavangeboteResponse:
    """Response-Element für den 1.

    Klang (SAV)
    """
    class Meta:
        name = "erstelleSAVAngeboteResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_response: Optional[AngebotsResponse] = field(
        default=None,
        metadata={
            "name": "angebotsResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ErstelleTarifWegKombinationsAngebotResponse:
    class Meta:
        name = "erstelleTarifWegKombinationsAngebotResponse"
        namespace = "http://nova.voev.ch/services/v14/vertrieb"

    angebots_response: Optional[AngebotsResponse] = field(
        default=None,
        metadata={
            "name": "angebotsResponse",
            "type": "Element",
            "required": True,
        }
    )
