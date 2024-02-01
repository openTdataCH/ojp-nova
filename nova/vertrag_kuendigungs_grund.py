from dataclasses import dataclass, field
from typing import Optional
from nova.localized_string import LocalizedString

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class VertragKuendigungsGrund:
    kuendigungs_grund_bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "kuendigungsGrundBezeichnung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
    kuendigungs_grund_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "kuendigungsGrundCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
        }
    )
