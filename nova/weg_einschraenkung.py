from dataclasses import dataclass, field
from typing import Optional
from nova.abstract_einschraenkung import AbstractEinschraenkung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class WegEinschraenkung:
    """@Deprecated will be removed in NOVA 15"""
    abgangs_einschraenkung: Optional[AbstractEinschraenkung] = field(
        default=None,
        metadata={
            "name": "abgangsEinschraenkung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    bestimmungs_einschraenkung: Optional[AbstractEinschraenkung] = field(
        default=None,
        metadata={
            "name": "bestimmungsEinschraenkung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    umkehr_moeglich: bool = field(
        default=False,
        metadata={
            "name": "umkehrMoeglich",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
