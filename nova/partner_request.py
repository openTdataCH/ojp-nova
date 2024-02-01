from dataclasses import dataclass, field
from typing import List, Optional
from nova.forciert import Forciert
from nova.korrespondenz_sprach_code import KorrespondenzSprachCode
from nova.qualitaets_eigenschaft import QualitaetsEigenschaft
from nova.qualitaets_wert import QualitaetsWert
from nova.sitz_request import SitzRequest
from nova.sprach_code import SprachCode
from nova.werbung import Werbung
from nova.werbung_bestaetigung import WerbungBestaetigung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class PartnerRequest:
    """
    Repräsentiert einen Partner (Person, Organisation) in Anfragen.

    :ivar sitz:
    :ivar festnetz:
    :ivar mobil:
    :ivar email:
    :ivar korrespondenz_sprache: @Deprecated will be removed in NOVA 15.
    :ivar sprache:
    :ivar werbung: Kennzeichnung ob der Kunde Werbung erhalten
        will/darf.
    :ivar werbung_bestaetigung: Angabe ob Benutzer
        Marketinginformationen erhält.
    :ivar forciertes_einfuegen:
    :ivar qualitaets_eigenschaft:
    """
    sitz: Optional[SitzRequest] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "nillable": True,
        }
    )
    festnetz: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 16,
        }
    )
    mobil: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 16,
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 255,
        }
    )
    korrespondenz_sprache: Optional[KorrespondenzSprachCode] = field(
        default=None,
        metadata={
            "name": "korrespondenzSprache",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "nillable": True,
        }
    )
    sprache: Optional[SprachCode] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    werbung: Optional[Werbung] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "nillable": True,
        }
    )
    werbung_bestaetigung: Optional[WerbungBestaetigung] = field(
        default=None,
        metadata={
            "name": "werbungBestaetigung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "nillable": True,
        }
    )
    forciertes_einfuegen: Optional[Forciert] = field(
        default=None,
        metadata={
            "name": "forciertesEinfuegen",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
    qualitaets_eigenschaft: List["PartnerRequest.QualitaetsEigenschaft"] = field(
        default_factory=list,
        metadata={
            "name": "qualitaetsEigenschaft",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )

    @dataclass
    class QualitaetsEigenschaft:
        """
        :ivar qualitaets_eigenschaft_code:
        :ivar qualitaets_wert: @Deprecated will be removed in NOVA 15.
        :ivar qualitaets_wert_code:
        """
        qualitaets_eigenschaft_code: Optional[QualitaetsEigenschaft] = field(
            default=None,
            metadata={
                "name": "qualitaetsEigenschaftCode",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
                "required": True,
            }
        )
        qualitaets_wert: Optional[QualitaetsWert] = field(
            default=None,
            metadata={
                "name": "qualitaetsWert",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
                "required": True,
            }
        )
        qualitaets_wert_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "qualitaetsWertCode",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            }
        )
