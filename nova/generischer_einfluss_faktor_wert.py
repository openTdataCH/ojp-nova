from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime
from nova.geld_betrag import GeldBetrag

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


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
