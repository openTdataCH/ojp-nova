from dataclasses import dataclass, field
from typing import List, Optional
from nova.paketbedingung import Paketbedingung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AngebotsPaket:
    """Ein AngebotsPaket, welches Alternativ- und/oder optionale Zusatzangebote
    beinhaltet, referenziert alle AngebotsPakete wofür das alternative
    AngebotsPaket eine Alternative oder Ergänzung (Zusatzangebote) ist.

    AngebotsPakete werden von NOVA nicht sortiert - diese Aufgabe liegt an LV

    :ivar angebot_refs: Verweist auf 1..* Angebote/SAVAngebote, die
        gemeinsam ein AngebotsPaket darstellen und gemeinsam gekauft
        werden sollten, um den Kundenwunsch abzudecken.
    :ivar reisender_refs: Verweist auf Reisende, für die dieses Angebot
        gültig ist.
    :ivar meldungen_refs:
    :ivar id:
    :ivar paketbedingung:
    """
    angebot_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "angebotRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "tokens": True,
        }
    )
    reisender_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "reisenderRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "tokens": True,
        }
    )
    meldungen_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "meldungenRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "tokens": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    paketbedingung: Optional[Paketbedingung] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
