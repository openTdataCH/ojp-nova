from dataclasses import dataclass, field
from typing import List, Optional
from nova.geld_betrag import GeldBetrag
from nova.mwst_anteil import MwstAnteil

__NAMESPACE__ = "http://nova.voev.ch/services/v14/base"


@dataclass
class Preis:
    """
    Repräsentiert einen Preis inklusive Mehrwertsteuer.

    :ivar geld_betrag:
    :ivar mwst_anteil: Gibt die MwSt Anteile des Preis an. Im Normalfall
        genau ein Element (100% des Preis mit demselben MwSt-Satz). Für
        Produkte mit Bausteinen, die unterschiedlichen MwSt-Sätzen
        unterliegen, werden mehrere Elemente geliefert.
    """
    geld_betrag: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "geldBetrag",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "required": True,
        }
    )
    mwst_anteil: List[MwstAnteil] = field(
        default_factory=list,
        metadata={
            "name": "mwstAnteil",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/base",
            "min_occurs": 1,
        }
    )
