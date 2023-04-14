from dataclasses import dataclass, field
from typing import List, Optional
from nova.abstract_angebot import AbstractAngebot
from nova.angebots_paket import AngebotsPaket
from nova.geltungs_bereich import GeltungsBereich
from nova.reisender import Reisender
from nova.verbindungs_info import VerbindungsInfo
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AngebotsResponse(VertriebsResponse):
    """
    Die Klasse Angebotsantwort dient als Container für die ermittelten Angebote
    und beinhaltet zusätzlich angebotsübergreifende Informationen.
    """
    angebote: Optional["AngebotsResponse.Angebote"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    reisende: Optional["AngebotsResponse.Reisende"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    angebots_pakete: Optional["AngebotsResponse.AngebotsPakete"] = field(
        default=None,
        metadata={
            "name": "angebotsPakete",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    geltungs_bereiche: Optional["AngebotsResponse.GeltungsBereiche"] = field(
        default=None,
        metadata={
            "name": "geltungsBereiche",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    verbindungen: Optional["AngebotsResponse.Verbindungen"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )

    @dataclass
    class Angebote:
        """
        :ivar angebot: Abhängig von der Anfrage (Angebotsanfrage,
            SAVAngebotsanfrage) sind hier Instanzen von Angebot oder
            SAVAngebot enthalten.
        """
        angebot: List[AbstractAngebot] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )

    @dataclass
    class Reisende:
        reisender: List[Reisender] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )

    @dataclass
    class AngebotsPakete:
        angebots_paket: List[AngebotsPaket] = field(
            default_factory=list,
            metadata={
                "name": "angebotsPaket",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )

    @dataclass
    class GeltungsBereiche:
        geltungs_bereich: List[GeltungsBereich] = field(
            default_factory=list,
            metadata={
                "name": "geltungsBereich",
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )

    @dataclass
    class Verbindungen:
        verbindung: List[VerbindungsInfo] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            }
        )
