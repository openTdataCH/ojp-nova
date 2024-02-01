from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class QualitaetsAnforderungDefinition:
    moegliche_qualitaets_eigenschaft_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "moeglicheQualitaetsEigenschaftRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
            "tokens": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
