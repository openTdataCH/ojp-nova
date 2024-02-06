from dataclasses import dataclass, field
from typing import List, Optional
from nova.generischer_einfluss_faktor_typ import GenerischerEinflussFaktorTyp
from nova.generischer_einfluss_faktor_wert import GenerischerEinflussFaktorWert
from nova.localized_string import LocalizedString

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class GenerischerEinflussFaktor:
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    druck_bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "druckBezeichnung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    moeglicher_wert: List["GenerischerEinflussFaktor.MoeglicherWert"] = field(
        default_factory=list,
        metadata={
            "name": "moeglicherWert",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    typ: Optional[GenerischerEinflussFaktorTyp] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )

    @dataclass
    class MoeglicherWert:
        wert_bezeichnung: Optional[LocalizedString] = field(
            default=None,
            metadata={
                "name": "wertBezeichnung",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            }
        )
        wert: Optional[GenerischerEinflussFaktorWert] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
                "required": True,
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
                "required": True,
            }
        )
