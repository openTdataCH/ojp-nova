from dataclasses import dataclass, field
from typing import List, Optional
from nova.abstract_angebot import AbstractAngebot
from nova.erstattungs_gebuehr import ErstattungsGebuehr
from nova.geld_betrag import GeldBetrag
from nova.zu_erstattende_leistung import ZuErstattendeLeistung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class Savangebot(AbstractAngebot):
    """
    Angebot für SAV (Erneuerung, Erstattung), die über SAVAngebotsanfrage
    angefordert wurde.

    :ivar zu_erstattende_leistung:
    :ivar total_erstattungs_betraege:
    :ivar max_selbstbehalt:
    :ivar angewendeter_selbstbehalt:
    :ivar min_selbstbehalt:
    :ivar erstattungs_gebuehr:
    :ivar ausweis_pflicht:
    :ivar traeger_medium: Aktuell konstant "SICHERHEITSPAPIER"
    """
    class Meta:
        name = "SAVAngebot"

    zu_erstattende_leistung: List[ZuErstattendeLeistung] = field(
        default_factory=list,
        metadata={
            "name": "zuErstattendeLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    total_erstattungs_betraege: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "totalErstattungsBetraege",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    max_selbstbehalt: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "maxSelbstbehalt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    angewendeter_selbstbehalt: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "angewendeterSelbstbehalt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    min_selbstbehalt: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "minSelbstbehalt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    erstattungs_gebuehr: List[ErstattungsGebuehr] = field(
        default_factory=list,
        metadata={
            "name": "erstattungsGebuehr",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    ausweis_pflicht: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ausweisPflicht",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    traeger_medium: Optional[str] = field(
        default=None,
        metadata={
            "name": "traegerMedium",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
