from dataclasses import dataclass, field
from typing import Optional
from nova.geld_betrag import GeldBetrag
from nova.gueltigkeits_zeitraum import GueltigkeitsZeitraum
from nova.produkt_einfluss_faktor_gruppe import ProduktEinflussFaktorGruppe

__NAMESPACE__ = "http://nova.voev.ch/services/v14/preisauskunft"


@dataclass
class PreisAuspraegung:
    produkt_einfluss_faktoren: Optional[ProduktEinflussFaktorGruppe] = field(
        default=None,
        metadata={
            "name": "produktEinflussFaktoren",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
        }
    )
    preis: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
    nutzungs_zeitraum: Optional[GueltigkeitsZeitraum] = field(
        default=None,
        metadata={
            "name": "nutzungsZeitraum",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
    externe_verbindungs_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeVerbindungsReferenzID",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "min_length": 0,
            "max_length": 50,
        }
    )
    externe_reisenden_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeReisendenReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
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
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
            "min_inclusive": 0,
        }
    )
    verfuegbares_kontingent: Optional[int] = field(
        default=None,
        metadata={
            "name": "verfuegbaresKontingent",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
        }
    )
