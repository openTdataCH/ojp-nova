from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlTime
from nova.angebots_filter import AngebotsFilter
from nova.fahrplan_verbindung import FahrplanVerbindung
from nova.klassen_typ_code import KlassenTypCode
from nova.reisenden_info import ReisendenInfo

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class OevAnfrageParameterType:
    fahrt_wunsch: Optional["OevAnfrageParameterType.FahrtWunsch"] = field(
        default=None,
        metadata={
            "name": "fahrtWunsch",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    reisender: List["OevAnfrageParameterType.Reisender"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    angebots_filter: List[AngebotsFilter] = field(
        default_factory=list,
        metadata={
            "name": "angebotsFilter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    traeger_medium: List[str] = field(
        default_factory=list,
        metadata={
            "name": "traegerMedium",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
    gewuenschte_klasse: List[KlassenTypCode] = field(
        default_factory=list,
        metadata={
            "name": "gewuenschteKlasse",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class FahrtWunsch:
        hin_fahrt_verbindung: Optional[FahrplanVerbindung] = field(
            default=None,
            metadata={
                "name": "hinFahrtVerbindung",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
        rueck_fahrt_verbindung: Optional[FahrplanVerbindung] = field(
            default=None,
            metadata={
                "name": "rueckFahrtVerbindung",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        datum_rueck_fahrt: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "datumRueckFahrt",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
        zeitpunkt_rueck_fahrt: Optional[XmlTime] = field(
            default=None,
            metadata={
                "name": "zeitpunktRueckFahrt",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )

    @dataclass
    class Reisender(ReisendenInfo):
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
