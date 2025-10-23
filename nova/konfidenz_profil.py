from dataclasses import dataclass, field
from typing import List, Optional
from nova.automatische_validierungen import AutomatischeValidierungen
from nova.partner_type import PartnerType

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class KonfidenzProfil:
    """
    Ein Konfidenzprofil definiert Anforderungen an einen Partner-Datensatz (Person,
    Organisation).

    :ivar automatische_validierungen: Beschreibt die Validierungen, die
        im Rahmen des Konfidenzprofils automatisch durch NOVAGP
        vorgenommen werden.
    :ivar qualitaets_anforderung_refs:
    :ivar pflichtfeld:
    :ivar name:
    :ivar kuba_store: Dies führt dazu, dass der Partner in KUBA abgelegt
        (und dadurch eine CKM angelegt) wird, sofern er noch nicht dort
        gespeichert ist. Die führt implizit dazu, dass eine Validierung
        gegen die KUBA-Regeln erfolgt ==&gt; Man sollte/muss parallel
        das Flag kubaCheck setzen.
    """
    automatische_validierungen: Optional[AutomatischeValidierungen] = field(
        default=None,
        metadata={
            "name": "automatischeValidierungen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    qualitaets_anforderung_refs: List[str] = field(
        default_factory=list,
        metadata={
            "name": "qualitaetsAnforderungRefs",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "tokens": True,
        }
    )
    pflichtfeld: List["KonfidenzProfil.Pflichtfeld"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
            "min_length": 0,
            "max_length": 64,
        }
    )
    kuba_store: Optional[bool] = field(
        default=None,
        metadata={
            "name": "kubaStore",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )

    @dataclass
    class Pflichtfeld:
        pfad: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
                "required": True,
                "min_length": 0,
                "max_length": 200,
            }
        )
        anwendbar_fuer: Optional[PartnerType] = field(
            default=None,
            metadata={
                "name": "anwendbarFuer",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
                "required": True,
            }
        )
