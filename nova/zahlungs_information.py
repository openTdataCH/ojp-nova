from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from nova.geld_betrag import GeldBetrag
from nova.zahlungs_art import ZahlungsArt
from nova.zahlungs_attribut import ZahlungsAttribut

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


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
    :ivar auslaendische_zahlung:
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
    auslaendische_zahlung: Optional["ZahlungsInformation.AuslaendischeZahlung"] = field(
        default=None,
        metadata={
            "name": "auslaendischeZahlung",
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
    class AuslaendischeZahlung:
        betrag: Optional[GeldBetrag] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
        angewendeter_wechselkurs: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "angewendeterWechselkurs",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "total_digits": 7,
                "fraction_digits": 5,
            }
        )
