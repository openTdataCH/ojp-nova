from dataclasses import dataclass, field
from typing import Optional
from nova.angebots_request import AngebotsRequest
from nova.klassen_typ_code import KlassenTypCode
from nova.strecke import Strecke
from nova.weg_suche import WegSuche

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class StreckenWechselAngebotsRequest(AngebotsRequest):
    bestehender_weg: Optional[WegSuche] = field(
        default=None,
        metadata={
            "name": "bestehenderWeg",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    strecke: Optional[Strecke] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    bestehende_klasse: Optional[KlassenTypCode] = field(
        default=None,
        metadata={
            "name": "bestehendeKlasse",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
