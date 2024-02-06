from dataclasses import dataclass, field
from typing import List
from nova.konfidenz_profil import KonfidenzProfil
from nova.qualitaets_anforderung_definition import QualitaetsAnforderungDefinition
from nova.qualitaets_eigenschafts_definition import QualitaetsEigenschaftsDefinition
from nova.rollen_definition import RollenDefinition

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class RollenStammdaten:
    rollen_definition: List[RollenDefinition] = field(
        default_factory=list,
        metadata={
            "name": "rollenDefinition",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    konfidenz_profil: List[KonfidenzProfil] = field(
        default_factory=list,
        metadata={
            "name": "konfidenzProfil",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    qualitaets_anforderung: List[QualitaetsAnforderungDefinition] = field(
        default_factory=list,
        metadata={
            "name": "qualitaetsAnforderung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    moegliche_qualitaets_eigenschaft: List[QualitaetsEigenschaftsDefinition] = field(
        default_factory=list,
        metadata={
            "name": "moeglicheQualitaetsEigenschaft",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
