from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class Adresse:
    """
    :ivar land:
    :ivar ort:
    :ivar plz:
    :ivar adress_zusatz:
    :ivar strasse_hnr:
    :ivar strassenname: Delivered only for CH/LI addresses if street and
        house number can be separated.
    :ivar hausnummer: Delivered only for CH/LI addresses if street and
        house number can be separated.
    :ivar postfach:
    :ivar postfach_vorhanden: Flag, das angibt, dass für den Partner ein
        Postfach vorhanden ist, obwohl dieses nicht explizit als
        "postfach" aufgeführt wird.
    """
    land: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 2,
            "max_length": 2,
            "pattern": r"[A-Z]{2}",
        }
    )
    ort: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 30,
        }
    )
    plz: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 15,
        }
    )
    adress_zusatz: Optional[str] = field(
        default=None,
        metadata={
            "name": "adressZusatz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 30,
        }
    )
    strasse_hnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "strasseHnr",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 30,
        }
    )
    strassenname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 30,
        }
    )
    hausnummer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 30,
        }
    )
    postfach: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 5,
        }
    )
    postfach_vorhanden: bool = field(
        default=False,
        metadata={
            "name": "postfachVorhanden",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )


@dataclass
class ClientIdentifier:
    """
    Ein ClientIdentfier identifiziert den anfragenden Client (Serviceaufrufer) aus
    fachlicher Sicht.

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


@dataclass
class CorrelationKontext:
    correlation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "correlationId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    geschaefts_prozess_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "geschaeftsProzessId",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )


class Currency(Enum):
    CHF = "CHF"
    EUR = "EUR"


@dataclass
class DatumsZeitraum:
    """Ermöglicht die Angabe eines Datumszeitraum (von/bis) ohne Uhrzeit.

    Siehe auch Zeitraum, AusweisbarerZeitraum.
    """
    von: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
    bis: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )


class GeschaeftsFeld(Enum):
    B2_B = "B2B"
    B2_C = "B2C"
    FVP = "FVP"


class Geschlecht(Enum):
    MAENNLICH = "MAENNLICH"
    WEIBLICH = "WEIBLICH"


class KanalTyp(Enum):
    AUTOMAT = "AUTOMAT"
    ONLINE = "ONLINE"
    BEDIENTER_VERKAUF = "BEDIENTER_VERKAUF"
    BATCH = "BATCH"


@dataclass
class LocalizedString:
    """Der Basisdatentyp LocalizedString wird für alle Texte / Zeichenketten
    verwendet, die auf der öV-Plattform internationalisiert werden.

    Das Objekt LocalizedString bietet in Abhängigkeit von der Locale die
    entsprechenden Übersetzungen der Texte / Zeichenketten.
    """
    default_wert: Optional[str] = field(
        default=None,
        metadata={
            "name": "defaultWert",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 4000,
        }
    )
    de: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 4000,
        }
    )
    en: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 4000,
        }
    )
    fr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 4000,
        }
    )
    it: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 4000,
        }
    )


@dataclass
class LocalizedText:
    value_de: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueDe",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 4000,
        }
    )
    value_en: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueEn",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 4000,
        }
    )
    value_fr: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueFr",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 4000,
        }
    )
    value_it: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueIt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 4000,
        }
    )


@dataclass
class LocalizedUrl:
    """
    Bietet sprachspezifische URLs.
    """
    class Meta:
        name = "LocalizedURL"

    default_wert: Optional[str] = field(
        default=None,
        metadata={
            "name": "defaultWert",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "max_length": 2048,
        }
    )
    de: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "max_length": 2048,
        }
    )
    en: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "max_length": 2048,
        }
    )
    fr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "max_length": 2048,
        }
    )
    it: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "max_length": 2048,
        }
    )


class MeldungsTyp(Enum):
    TECHNISCHER_FEHLER = "TECHNISCHER_FEHLER"
    FEHLER = "FEHLER"
    WARNUNG = "WARNUNG"
    INFORMATION = "INFORMATION"


@dataclass
class MwstAnteil:
    betrag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "total_digits": 12,
            "fraction_digits": 2,
            "pattern": r"-?[0-9]{1,10}(\.[0-9]{0,2})?",
        }
    )
    mwst_satz: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "mwstSatz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )


@dataclass
class NameVorname:
    """
    :ivar name:
    :ivar vorname:
    :ivar version_name: will be mandatory in NOVA 15
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 30,
        }
    )
    vorname: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 30,
        }
    )
    version_name: Optional[int] = field(
        default=None,
        metadata={
            "name": "versionName",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )


class Operator(Enum):
    """@Deprecated Will be removed in NOVA 15. Definiert, wie im Feld nach dem Suchbegriff gesucht wird (z.B. gleich, grösser oder gleich, kleiner oder gleich)."""
    GLEICH = "GLEICH"
    GROESSER_GLEICH = "GROESSER_GLEICH"
    KLEINER_GLEICH = "KLEINER_GLEICH"


@dataclass
class PagingParameter:
    """
    Trefferanzahl und -offset für die Suche.
    """
    max_treffer: Optional[int] = field(
        default=None,
        metadata={
            "name": "maxTreffer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_inclusive": 0,
        }
    )
    treffer_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "trefferOffset",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_inclusive": 0,
        }
    )


class SprachCode(Enum):
    """Die in NOVA unterstützten ISO Sprachcodes gemäss ISO 639-1 (Nur
    Kleinbuchstaben erlaubt).

    Aktuell sind das: de, fr, it, en.
    """
    DE = "de"
    EN = "en"
    FR = "fr"
    IT = "it"


@dataclass
class SystemInformation:
    plattform_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "plattformVersion",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )


@dataclass
class TelefonNummerFormatiert:
    """
    :ivar wert:
    :ivar formatiert_e123: @Deprecated Will be removed with NOVA 15.
        Phone number can be formatted by client with for example
        libphonenumber (https://github.com/google/libphonenumber)
    :ivar version_telefon_nummer:
    """
    wert: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 16,
        }
    )
    formatiert_e123: Optional[str] = field(
        default=None,
        metadata={
            "name": "formatiertE123",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_length": 0,
            "max_length": 16,
        }
    )
    version_telefon_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "versionTelefonNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )


@dataclass
class TimeShift:
    """Ein TimeShift kann optional einer VertriebsAnfrage mitgegeben werden, um den
    Anfragezeitpunkt künstlich zu verschieben. Ein TimeShift besteht aus:

    - einer optionalen Anfragezeit, welche festgelegt werden kann
    - einem optionalen AnfrageDatumShift, welches das Anfragedatum entweder fix, oder per Delta festlegen kann
    Eines der beiden optionalen Attribute muss jeweils gesetzt sein, es dürfen nicht beide gleichzeitig leer sein.
    """
    anfrage_datum_shift: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "anfrageDatumShift",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
    anfrage_zeit: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "anfrageZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )


@dataclass
class UhrzeitAbschnitt:
    von: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
    bis: Optional[XmlTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )


class WochenTag(Enum):
    MONTAG = "MONTAG"
    DIENSTAG = "DIENSTAG"
    MITTWOCH = "MITTWOCH"
    DONNERSTAG = "DONNERSTAG"
    FREITAG = "FREITAG"
    SAMSTAG = "SAMSTAG"
    SONNTAG = "SONNTAG"


class ZahlungsIntervall(Enum):
    MONATLICH = "MONATLICH"
    JAEHRLICH = "JAEHRLICH"


class ZeitEinheitCode(Enum):
    """Code der eine Zeiteinheit eindeutig identifiziert.

    MINUTEN; STUNDEN; TAGE; WOCHEN; MONATE; JAHRE
    """
    MINUTEN = "MINUTEN"
    STUNDEN = "STUNDEN"
    TAGE = "TAGE"
    WOCHEN = "WOCHEN"
    MONATE = "MONATE"
    JAHRE = "JAHRE"


@dataclass
class Zeitraum:
    """Ermöglicht die Angabe eines Zeitraum (von/bis) mit Uhrzeit.

    Siehe auch DatumZeitraum, AusweisbarerZeitraum.
    """
    von: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
    bis: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )


@dataclass
class GeldBetrag:
    """
    Der GeldBetrag wird definiert durch einen Betrag und eine Währung.

    :ivar betrag: beziffert den GeldBetrag
    :ivar waehrung:
    """
    betrag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "total_digits": 12,
            "fraction_digits": 2,
            "pattern": r"-?[0-9]{1,10}(\.[0-9]{0,2})?",
        }
    )
    waehrung: Optional[Currency] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )


@dataclass
class Kanal:
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
    kanal_typ: Optional[KanalTyp] = field(
        default=None,
        metadata={
            "name": "kanalTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    geschaefts_feld: Optional[GeschaeftsFeld] = field(
        default=None,
        metadata={
            "name": "geschaeftsFeld",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    bezeichnung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 200,
        }
    )


@dataclass
class Meldung:
    """
    Eine fachliche oder technische Meldung des Systems, die für Clients von
    Bedeutung sein kann.

    :ivar beschreibung:
    :ivar id: Technische ID zur Referenzierung innerhalb des XML-
        Dokuments. Wird nur gesetzt für Meldungen, die auch von anderer
        Stelle referenziert werden (Klang 1-4 Antworten).
    :ivar meldungs_code: Code, der eine Meldung eindeutig identifiziert.
    :ivar zeit_stempel:
    :ivar typ: TECHNISCHER_FEHLER bei technischen Fehlern (z.B.
        Nichtverfügbarkeit von Partnersystemen, alle anderen Typen
        kennzeichnen fachliche Meldungen.
    :ivar end_kunden_relevant: true, falls der Meldungstext für einen
        Endkunden relevant ist. Default=false.
    """
    beschreibung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )
    meldungs_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "meldungsCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    zeit_stempel: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "zeitStempel",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    typ: Optional[MeldungsTyp] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    end_kunden_relevant: Optional[bool] = field(
        default=None,
        metadata={
            "name": "endKundenRelevant",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )


@dataclass
class ZeitEinheit:
    """
    Eine Auflistung möglicher Zeiteinheiten.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    code: Optional[ZeitEinheitCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )


@dataclass
class Dauer:
    """
    Aggregation von Wert und Einheit.
    """
    wert: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
            "min_inclusive": 0,
        }
    )
    einheit: Optional[ZeitEinheit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )


@dataclass
class Meldungen:
    meldung: List[Meldung] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
        }
    )


@dataclass
class Preis:
    """
    Repräsentiert einen Preis inklusive Mehrwertsteuer.

    :ivar geld_betrag:
    :ivar mwst_anteil: Gibt die MwSt Anteile des Preis an. Im Normalfall
        genau ein Element (100% des Preis mit demselben MwSt-Satz). Für
        Produkte mit Bausteinen, die unterschiedlichen MwSt-Sätzen
        unterliegen, werden mehrere Elemente geliefert.
    """
    geld_betrag: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "geldBetrag",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    mwst_anteil: List[MwstAnteil] = field(
        default_factory=list,
        metadata={
            "name": "mwstAnteil",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_occurs": 1,
        }
    )
