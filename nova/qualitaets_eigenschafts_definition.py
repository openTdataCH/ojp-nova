from dataclasses import dataclass, field
from typing import List, Optional
from nova.qualitaets_eigenschaft import QualitaetsEigenschaft
from nova.qualitaets_wert import QualitaetsWert

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class QualitaetsEigenschaftsDefinition:
    """
    :ivar moeglicher_qualitaets_wert: @Deprecated will be removed in
        NOVA 15.
    :ivar moeglicher_qualitaets_wert_code:
    :ivar id:
    :ivar qualitaets_eigenschafts_code:
    """
    moeglicher_qualitaets_wert: List[QualitaetsWert] = field(
        default_factory=list,
        metadata={
            "name": "moeglicherQualitaetsWert",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_occurs": 1,
        }
    )
    moeglicher_qualitaets_wert_code: List[str] = field(
        default_factory=list,
        metadata={
            "name": "moeglicherQualitaetsWertCode",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_occurs": 1,
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
    qualitaets_eigenschafts_code: Optional[QualitaetsEigenschaft] = field(
        default=None,
        metadata={
            "name": "qualitaetsEigenschaftsCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
