from dataclasses import dataclass, field
from typing import Optional
from nova.dauer import Dauer
from nova.erneuerungs_art import ErneuerungsArt
from nova.erneuerungs_art_grund import ErneuerungsArtGrund
from nova.kauf_art import KaufArt
from nova.zahlungs_intervall import ZahlungsIntervall

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


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
