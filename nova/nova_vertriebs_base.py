from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime
from nova.nova_base import (
    Adresse,
    GeldBetrag,
    LocalizedString,
    NameVorname,
)

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class AngebotsFilter:
    """Mittels Angebotsfilter werden die möglichen Angebote auf eine bestimmte
    Menge eingeschränkt und gefiltert.

    Die Klasse Angebotsfilter selbst ist abstrakt und wird in der Form
    von angegebenen ProduktNummern und/oder ProdukteListeFiltern
    konkretisiert.
    """


@dataclass
class AusweisbarerZeitraum:
    """Ermöglicht die Angabe eines Zeitraum (von/bis) mit separater Angabe von
    Datum und Uhrzeit.

    Siehe auch Zeitraum, DatumZeitraum. Darf lediglich zu Ausgabezwecken
    (Druck / Screenanzeige) verwendet werden.
    """
    von: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    von_zeit: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "vonZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    bis_zeit: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "bisZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )


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
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_occurs": 1,
            "min_length": 0,
            "max_length": 32,
        }
    )


class DruckAttributTyp(Enum):
    TEXT = "TEXT"
    LOCALIZEDTEXT = "LOCALIZEDTEXT"
    GANZZAHL = "GANZZAHL"
    DEZIMALZAHL = "DEZIMALZAHL"
    DATUM = "DATUM"
    ZEIT = "ZEIT"
    DATUMZEIT = "DATUMZEIT"
    BINARY = "BINARY"
    GELDBETRAG = "GELDBETRAG"
    WEGANGABE = "WEGANGABE"
    BOOLEAN = "BOOLEAN"
    REISEWEGINFO = "REISEWEGINFO"


@dataclass
class EmptyType:
    """
    The empty type, containing neither attributes nor elements, used as Wildcard in
    Taxonomieklassepfad.
    """


class ErneuerungsArt(Enum):
    GESTUETZT = "GESTUETZT"
    AUTOMATISCH = "AUTOMATISCH"
    NICHT_ERNEUERBAR = "NICHT_ERNEUERBAR"


class ErneuerungsArtGrund(Enum):
    VERTRAG = "VERTRAG"
    U16 = "U16"
    U18 = "U18"
    TEMP_WOHNSITZ = "TEMP_WOHNSITZ"
    ENTFERNTES_AUSLAND = "ENTFERNTES_AUSLAND"
    GESTUETZT = "GESTUETZT"


class ErstattungsTyp(Enum):
    VOLLERSTATTUNG = "VOLLERSTATTUNG"
    TEILERSTATTUNG = "TEILERSTATTUNG"
    ANNULLATION = "ANNULLATION"
    HINTERLEGUNG = "HINTERLEGUNG"


class FahrArtTypCode(Enum):
    """Mittels FahrartTypCode ist ein FahrartTyp eindeutig zu identifizieren.

    Diese Klasse ist für Anfragen zu referenzieren. Der Fahrarttyp
    enthält alle wählbaren Fahrarten: EINFACH; RETOUR; RUNDFAHRT
    """
    EINFACH = "EINFACH"
    RETOUR = "RETOUR"
    RUNDFAHRT = "RUNDFAHRT"


class FahrAusweisArt(Enum):
    EINZELBILLETT = "EINZELBILLETT"
    MEHRFAHRTENKARTE = "MEHRFAHRTENKARTE"
    ABONNEMENT = "ABONNEMENT"
    GRUPPE = "GRUPPE"


class GenerischerEinflussFaktorTyp(Enum):
    DATUM = "DATUM"
    ZEIT = "ZEIT"
    DATUMZEIT = "DATUMZEIT"
    TEXT = "TEXT"
    GANZZAHL = "GANZZAHL"
    DEZIMALZAHL = "DEZIMALZAHL"
    BOOLEAN = "BOOLEAN"
    LAND = "LAND"
    GELDBETRAG = "GELDBETRAG"


@dataclass
class Haltestelle:
    """Entspricht einem Knoten im Verkehrsnetz.

    Wird verwendet um den Weg eines Verkehrsangebots zu beschreiben.
    """
    bav_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "bavName",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_length": 0,
            "max_length": 64,
        }
    )
    koordinate_x: Optional[int] = field(
        default=None,
        metadata={
            "name": "koordinateX",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    koordinate_y: Optional[int] = field(
        default=None,
        metadata={
            "name": "koordinateY",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    uic_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "uicCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_inclusive": 0,
        }
    )


class KlassenTypCode(Enum):
    """Der KlassenTypCode enthält die Klassenspanne für den anfragenden
    Leistungsvermittler, das heisst die Menge aller wählbaren Klassen.

    KLASSE_1; KLASSE_2; KLASSENWECHSEL Mittels KlassenTypCode ist eine
    Klasse eindeutig zu identifizieren. Diese Klasse ist für Anfragen zu
    referenzieren.
    """
    KLASSE_1 = "KLASSE_1"
    KLASSE_2 = "KLASSE_2"
    KLASSENWECHSEL = "KLASSENWECHSEL"


@dataclass
class Parkplatz:
    """
    Repräsentiert Element Parkplatz  (ParkplatzCode und Bezeichnung)
    """
    bezeichnung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    parkplatz_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "parkplatzCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "max_inclusive": 9999999,
        }
    )


class RabattKlasse(Enum):
    B2_B = "B2B"
    FREIZEIT = "FREIZEIT"


class ReisendenTypCode(Enum):
    """
    PERSON; HUND; VELO.
    """
    PERSON = "PERSON"
    HUND = "HUND"
    VELO = "VELO"


class SegmentTyp(Enum):
    HALTESTELLE = "HALTESTELLE"
    INFO = "INFO"
    VERKEHRSMITTEL_TYP = "VERKEHRSMITTEL_TYP"
    TU = "TU"
    SEPARATOR = "SEPARATOR"
    ZONE = "ZONE"
    FAHRART = "FAHRART"
    VIA = "VIA"
    VERBUND = "VERBUND"
    LOKALNETZ = "LOKALNETZ"
    IP_VIATEXT = "IP_VIATEXT"


@dataclass
class StreckenWegMetaDaten:
    anzahl_verbindungen: Optional[int] = field(
        default=None,
        metadata={
            "name": "anzahlVerbindungen",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "max_inclusive": 9999,
        }
    )
    mindest_anzahl_umstiege: Optional[int] = field(
        default=None,
        metadata={
            "name": "mindestAnzahlUmstiege",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "max_inclusive": 99,
        }
    )
    schnellste_reise_dauer: Optional[int] = field(
        default=None,
        metadata={
            "name": "schnellsteReiseDauer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "max_inclusive": 9999,
        }
    )


class TarifKlasse(Enum):
    DV = "DV"
    VERBUND = "VERBUND"
    IP = "IP"
    INTER = "INTER"
    FREIZEIT = "FREIZEIT"
    SERVICE = "SERVICE"
    TU_TARIF = "TU_TARIF"
    VERBUNDERWEITERUNG = "VERBUNDERWEITERUNG"


class UhrzeitEinschraenkungenTyp(Enum):
    MIT_UHRZEITEINSCHRAENKUNGEN = "MIT_UHRZEITEINSCHRAENKUNGEN"
    OHNE_UHRZEITEINSCHRAENKUNGEN = "OHNE_UHRZEITEINSCHRAENKUNGEN"


class VerbundStreckenTyp(Enum):
    LANGSTRECKE = "LANGSTRECKE"
    KURZSTRECKE = "KURZSTRECKE"


class VerkaufsParameterWertTyp(Enum):
    """
    Enumeration aller möglichen VerkaufsParameter.
    """
    DATUM = "DATUM"
    ZEIT = "ZEIT"
    DATUMZEIT = "DATUMZEIT"
    TEXT = "TEXT"
    GANZZAHL = "GANZZAHL"
    DEZIMALZAHL = "DEZIMALZAHL"
    BOOLEAN = "BOOLEAN"
    TKID = "TKID"
    ADRESSE = "ADRESSE"
    NAMEVORNAME = "NAMEVORNAME"
    LAND = "LAND"


class VerkehrsMittelTypCode(Enum):
    """Mittels VerkehrsMittelTypCode ist ein VerkehrsMittel eindeutig zu
    identifizieren.

    Diese Klasse ist für Anfragen zu referenzieren. BAHN; BUS; SCHIFF
    """
    BAHN = "BAHN"
    SCHIFF = "SCHIFF"
    BUS = "BUS"


@dataclass
class ZahlungsAttribut:
    """Beliebige Attribute, die ein LV zu einem Zahlvorgang abspeichern kann.

    Wird z.B: von B2B verwendet, um in gewissen Situationen die
    RechnungsStelle und die Kostenzuordnung zu übergeben.
    """
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 200,
        }
    )


class ZonenBefahrungsTyp(Enum):
    RAUMZEIT = "RAUMZEIT"
    STRECKEZEIT = "STRECKEZEIT"


@dataclass
class ErstattungsGrundTyp:
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class FahrArtTyp:
    """
    Ein FahrartTyp kann sein Einfach, Retour oder Rundfahrt.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    code: Optional[FahrArtTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )


@dataclass
class GenerischerEinflussFaktorWert:
    datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    zeit: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    datum_zeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "datumZeit",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_length": 0,
            "max_length": 200,
        }
    )
    ganz_zahl: Optional[int] = field(
        default=None,
        metadata={
            "name": "ganzZahl",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    dezimal_zahl: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "dezimalZahl",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    boolean: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    land: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_length": 2,
            "max_length": 2,
            "pattern": r"[A-Z]{2}",
        }
    )
    geld_betrag: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "geldBetrag",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )


@dataclass
class KlassenTyp:
    """Der KlassenTyp enthält die Klassenspanne für den anfragenden
    Leistungsvermittler, das heisst die Menge aller wählbaren Klassen.

    Repräsentiert die Klasse, in der die Reise angetreten werden kann.
    Bspw. 1. Klasse oder 2. Klasse.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    code: Optional[KlassenTypCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )


@dataclass
class MoeglicheParkplatz(Parkplatz):
    gueltig_ab: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigAb",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    gueltig_bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "gueltigBis",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )


@dataclass
class ProduktNummerFilter(AngebotsFilter):
    """
    Ein Angebotsfilter, der ein Produkt eindeutig identifiziert.
    """
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_inclusive": 0,
        }
    )


@dataclass
class ReiseRouteSegment:
    """Die Generalisierung ReiserouteSegment steht für verschiedene Typen von
    Segmenten aus denen (durch Aneinanderreihung) eine für den Kunden relevante
    Information (bzgl.

    des Reisewegs und der ReisendenInfo) aufgebaut werden kann.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    segment_typ: Optional[SegmentTyp] = field(
        default=None,
        metadata={
            "name": "segmentTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    uic_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "uicCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_inclusive": 0,
        }
    )
    fahr_art_typ: Optional[FahrArtTypCode] = field(
        default=None,
        metadata={
            "name": "fahrArtTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    verkehrs_mittel_typ: Optional[VerkehrsMittelTypCode] = field(
        default=None,
        metadata={
            "name": "verkehrsMittelTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )


@dataclass
class TaxonomieKlassePfad:
    """
    :ivar wildcard: Leeres XML-Element. Anzugeben, um auf der
        vorliegenden Ebene jeden Klassennamen zu matchen (a.k.a. "*").
    :ivar klassen_name: Name der Taxonomieklasse, der auf der
        vorliegenden Ebene gematcht wird.
    """
    wildcard: Optional[EmptyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    klassen_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "klassenName",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_length": 0,
            "max_length": 200,
        }
    )


@dataclass
class TraegerMediumTyp:
    """Medium, auf dem die für die Kontrolle und den Kunden relevanten
    Informationen aufgedruckt bzw.

    angezeigt werden. Das Medium kann in physischer oder elektronischer
    Form sein.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    beschreibung_screen: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "beschreibungScreen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    beschreibung_ausgabe: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "beschreibungAusgabe",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class VerkaufsParameterWert:
    datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    zeit: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    datum_zeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "datumZeit",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_length": 0,
            "max_length": 200,
        }
    )
    ganz_zahl: Optional[int] = field(
        default=None,
        metadata={
            "name": "ganzZahl",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    dezimal_zahl: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "dezimalZahl",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    boolean: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    tkid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    adresse: Optional[Adresse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    name_vorname: Optional[NameVorname] = field(
        default=None,
        metadata={
            "name": "nameVorname",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    land: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_length": 2,
            "max_length": 2,
            "pattern": r"[A-Z]{2}",
        }
    )


@dataclass
class ZahlungsArt:
    """
    :ivar bezeichnung:
    :ivar zahlungs_art_code: UNBEKANNT; BAR; BON; MAE; FAK; DOS; DIN;
        AMX; JCB; VEG; VIS; PCD; YWD; MC; EC; MIG; ONE; REK; UAP
    :ivar kurz_text:
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    zahlungs_art_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "zahlungsArtCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    kurz_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "kurzText",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_length": 0,
            "max_length": 200,
        }
    )


@dataclass
class ZeitlicheFlexibilitaet:
    uhrzeit_einschraenkungen: Optional[UhrzeitEinschraenkungenTyp] = field(
        default=None,
        metadata={
            "name": "uhrzeitEinschraenkungen",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    zonen_befahrungs_typ: Optional[ZonenBefahrungsTyp] = field(
        default=None,
        metadata={
            "name": "zonenBefahrungsTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )


@dataclass
class ReiseWegInfo:
    """Die Reiseroute setzt sich aus mehreren geordneten ReiserouteSegmenten
    zusammen.

    Die Summe aller aneinandergereihter Segmente ergibt die Beschreibung
    einer Reiseroute.
    """
    abgang: Optional[ReiseRouteSegment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    bestimmung: Optional[ReiseRouteSegment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    reise_route_segment: List[ReiseRouteSegment] = field(
        default_factory=list,
        metadata={
            "name": "reiseRouteSegment",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    strecken_weg_meta_daten: Optional[StreckenWegMetaDaten] = field(
        default=None,
        metadata={
            "name": "streckenWegMetaDaten",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )


@dataclass
class TaxonomieFilter(AngebotsFilter):
    """
    Erlaubt die Filterung von Angeboten über Produkttaxonomien.

    :ivar produkt_taxonomie: Name der zu verwendenden Produkttaxonomie
    :ivar taxonomie_klasse_pfad: Geordnete Sequenz von Pfadangaben, mit
        der in der gewählten Produkttaxonomie die Taxonomieklassen
        ausgewählt werden, die dieser Filter anwenden soll. Beispiel:
        Die Sequenz ["Einzel", wildcard, "DV"] wählt alle
        Taxonomieklassen aus, die unterhalb "Einzel", dann irgend einer
        Klasse, dann "DV" liegen.
    """
    produkt_taxonomie: Optional[str] = field(
        default=None,
        metadata={
            "name": "produktTaxonomie",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 200,
        }
    )
    taxonomie_klasse_pfad: List[TaxonomieKlassePfad] = field(
        default_factory=list,
        metadata={
            "name": "taxonomieKlassePfad",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_occurs": 1,
        }
    )


@dataclass
class VerkaufsParameterTyp:
    """
    VerkaufsParameterTypen geben dem Leistungsvermittler an, welche Daten für die
    Offerte einer Leistung zwingend anzugeben sind.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    moeglicher_wert: List[VerkaufsParameterWert] = field(
        default_factory=list,
        metadata={
            "name": "moeglicherWert",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    wert: Optional[VerkaufsParameterWert] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    wert_typ: Optional[VerkaufsParameterWertTyp] = field(
        default=None,
        metadata={
            "name": "wertTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    format_einschraenkung: Optional[str] = field(
        default=None,
        metadata={
            "name": "formatEinschraenkung",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )


@dataclass
class WegAngabe:
    """
    Die Wegangabe beschreibt die tarifarische Gültigkeit in textueller Form und
    wird zu Kontrollzwecken aufs Ticket aufgedruckt.
    """
    abgang: Optional[ReiseRouteSegment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    bestimmung: Optional[ReiseRouteSegment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    reise_route_segment: List[ReiseRouteSegment] = field(
        default_factory=list,
        metadata={
            "name": "reiseRouteSegment",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    tarif_klasse: Optional[TarifKlasse] = field(
        default=None,
        metadata={
            "name": "tarifKlasse",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )


@dataclass
class DruckAttribut:
    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 200,
        }
    )
    typ: Optional[DruckAttributTyp] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    label: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_length": 0,
            "max_length": 4000,
        }
    )
    localized_text: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "localizedText",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    ganz_zahl: Optional[int] = field(
        default=None,
        metadata={
            "name": "ganzZahl",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    dezimal_zahl: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "dezimalZahl",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    zeit: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    datum_zeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "datumZeit",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    binary: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "format": "base64",
        }
    )
    geld_betrag: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "geldBetrag",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    weg_angabe: List[WegAngabe] = field(
        default_factory=list,
        metadata={
            "name": "wegAngabe",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    reise_weg_info: List[ReiseWegInfo] = field(
        default_factory=list,
        metadata={
            "name": "reiseWegInfo",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    boolean: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )


@dataclass
class DruckBeleg:
    traeger_medium_typ: Optional[TraegerMediumTyp] = field(
        default=None,
        metadata={
            "name": "traegerMediumTyp",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    druck_attribut: List[DruckAttribut] = field(
        default_factory=list,
        metadata={
            "name": "druckAttribut",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    beleg_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "belegId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_inclusive": 0,
        }
    )
    beleg_typ: Optional[str] = field(
        default=None,
        metadata={
            "name": "belegTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    produkt_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "produktNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "min_inclusive": 0,
        }
    )
