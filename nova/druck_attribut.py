from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlTime
from nova.druck_attribut_typ import DruckAttributTyp
from nova.geld_betrag import GeldBetrag
from nova.localized_string import LocalizedString
from nova.reise_weg_info import ReiseWegInfo
from nova.weg_angabe import WegAngabe

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


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
