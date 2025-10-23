from dataclasses import dataclass, field
from typing import List, Optional
from nova.localized_string import LocalizedString

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class ReisendenBeziehung:
    """
    :ivar bezeichnung:
    :ivar eingeschlossene_reisenden_beziehung: Reisendenbeziehungen, die
        von der vorliegenden Reisendenbeziehung eingeschlossen werden
        (z.B. ERWACHSENER_REIST_MIT schliesst KEINE_REISENDENBEZIEHUNG
        ein).
    :ivar moegliche_reisenden_beziehung: Reisendenbeziehungen, die von
        der vorliegenden Reisendenbeziehung eingeschlossen werden,
        sofern zusätzliche Bedingungen erfüllt sind (z.B.
        ERWACHSENER_REIST_MIT schliesst ELTERNTEIL_REIST_MIT ein, wenn
        Kind tatsächlich von Elternteil begleitet wird).
    :ivar code:
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    eingeschlossene_reisenden_beziehung: List[str] = field(
        default_factory=list,
        metadata={
            "name": "eingeschlosseneReisendenBeziehung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 0,
            "max_length": 50,
        }
    )
    moegliche_reisenden_beziehung: List[str] = field(
        default_factory=list,
        metadata={
            "name": "moeglicheReisendenBeziehung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 0,
            "max_length": 50,
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
