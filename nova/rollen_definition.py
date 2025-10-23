from dataclasses import dataclass, field
from typing import List, Optional
from nova.gesperrtes_attribut import GesperrtesAttribut
from nova.rollen_zugriff import RollenZugriff

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class RollenDefinition:
    create_role: List[RollenZugriff] = field(
        default_factory=list,
        metadata={
            "name": "createRole",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    delete_role: List[RollenZugriff] = field(
        default_factory=list,
        metadata={
            "name": "deleteRole",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    view_role: List[RollenZugriff] = field(
        default_factory=list,
        metadata={
            "name": "viewRole",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    update_partner: List[RollenZugriff] = field(
        default_factory=list,
        metadata={
            "name": "updatePartner",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    fuer_update_gesperrt: List[GesperrtesAttribut] = field(
        default_factory=list,
        metadata={
            "name": "fuerUpdateGesperrt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    rolle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
            "min_length": 0,
            "max_length": 64,
        }
    )
    konfidenz_profil: Optional[str] = field(
        default=None,
        metadata={
            "name": "konfidenzProfil",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
            "min_length": 0,
            "max_length": 64,
        }
    )
