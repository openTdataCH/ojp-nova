from dataclasses import dataclass, field
from typing import List, Optional
from nova.alters_bereich import AltersBereich
from nova.ermaessigungs_karte import ErmaessigungsKarte
from nova.geschlecht import Geschlecht
from nova.localized_string import LocalizedString
from nova.nachweis_kategorie import NachweisKategorie
from nova.reisenden_beziehung import ReisendenBeziehung
from nova.reisenden_typ_code import ReisendenTypCode

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class KundenSegment:
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    alters_bereich: Optional[AltersBereich] = field(
        default=None,
        metadata={
            "name": "altersBereich",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    ermaessigungs_karte: Optional[ErmaessigungsKarte] = field(
        default=None,
        metadata={
            "name": "ermaessigungsKarte",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    reisenden_beziehung: Optional[ReisendenBeziehung] = field(
        default=None,
        metadata={
            "name": "reisendenBeziehung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    kunden_segment_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "kundenSegmentRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "tokens": True,
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
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    reisenden_typ: Optional[ReisendenTypCode] = field(
        default=None,
        metadata={
            "name": "reisendenTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    geschlecht: Optional[Geschlecht] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    nachweis: Optional[NachweisKategorie] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
