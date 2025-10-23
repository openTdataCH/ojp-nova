from dataclasses import dataclass, field
from typing import Optional
from nova.generischer_einfluss_faktor_typ import GenerischerEinflussFaktorTyp
from nova.generischer_einfluss_faktor_wert import GenerischerEinflussFaktorWert
from nova.localized_string import LocalizedString

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


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
