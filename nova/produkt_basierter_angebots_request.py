from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlTime
from nova.angebots_request import AngebotsRequest
from nova.dauer import Dauer
from nova.geld_betrag import GeldBetrag

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


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
