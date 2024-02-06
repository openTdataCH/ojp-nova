from dataclasses import dataclass, field
from typing import List
from nova.abstract_einschraenkung import AbstractEinschraenkung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class HaltestellenEinschraenkung(AbstractEinschraenkung):
    """
    :ivar haltestelle_refs: @Deprecated will be removed in NOVA 15
    :ivar abgangs_haltestellen:
    :ivar bestimmungs_haltestellen:
    """
    haltestelle_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "haltestelleRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "tokens": True,
        }
    )
    abgangs_haltestellen: List[str] = field(
        default_factory=list,
        metadata={
            "name": "abgangsHaltestellen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "tokens": True,
        }
    )
    bestimmungs_haltestellen: List[str] = field(
        default_factory=list,
        metadata={
            "name": "bestimmungsHaltestellen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "tokens": True,
        }
    )
