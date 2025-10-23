from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlTime
from nova.angebots_request import AngebotsRequest
from nova.geld_betrag import GeldBetrag
from nova.verbund_strecken_request import VerbundStreckenRequest
from nova.zonen_request import ZonenRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


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
