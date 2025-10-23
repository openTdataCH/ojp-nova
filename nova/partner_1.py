from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from nova.forciert import Forciert
from nova.korrespondenz_sprach_code import KorrespondenzSprachCode
from nova.qualitaets_eigenschaft import QualitaetsEigenschaft
from nova.qualitaets_wert import QualitaetsWert
from nova.sitz import Sitz
from nova.sprach_code import SprachCode
from nova.telefon_nummer_formatiert import TelefonNummerFormatiert
from nova.werbung import Werbung
from nova.werbung_bestaetigung import WerbungBestaetigung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class Partner1:
    """
    Repräsentiert einen Partner (Person, Organisation) in Responses.

    :ivar sitz: Wohnsitz oder Unternehmenssitz.
    :ivar verknuepfte_tkid: {read-only} Die mit diesem Partner
        zusätzlich verknüpften TKIDs, die die Haupt-TKID des Partners
        referenzieren.
    :ivar qualitaets_eigenschaft:
    :ivar festnetz:
    :ivar mobil:
    :ivar tkid: {read-only} Haupt-TKID des Partners.
    :ivar ckm: {read-only}
    :ivar grundkarten_nummer: {read-only}
    :ivar email:
    :ivar korrespondenz_sprache: @Deprecated will be removed in NOVA 15,
        please use "sprache" instead.
    :ivar sprache:
    :ivar mut_datum: {read-only} Datum und Zeit der letzten Änderung
        dieses Objekts.
    :ivar forcierung: {read-only} Gibt an, ob bestimmte Attributwerte
        des Partners beim Anlegen/Aendern forciert wurden.
    :ivar werbung: Kennzeichnung ob der Kunde Werbung erhalten
        will/darf.
    :ivar werbung_bestaetigung: Angabe ob Benutzer
        Marketinginformationen erhält.
    :ivar version_partner:
    :ivar version_email:
    """
    class Meta:
        name = "Partner"

    sitz: Optional[Sitz] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    verknuepfte_tkid: List[str] = field(
        default_factory=list,
        metadata={
            "name": "verknuepfteTkid",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    qualitaets_eigenschaft: List["Partner1.QualitaetsEigenschaft"] = field(
        default_factory=list,
        metadata={
            "name": "qualitaetsEigenschaft",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    festnetz: Optional[TelefonNummerFormatiert] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    mobil: Optional[TelefonNummerFormatiert] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    tkid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
            "length": 36,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    ckm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 13,
        }
    )
    grundkarten_nummer: Optional[str] = field(
        default=None,
        metadata={
            "name": "grundkartenNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 6,
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 255,
        }
    )
    korrespondenz_sprache: Optional[KorrespondenzSprachCode] = field(
        default=None,
        metadata={
            "name": "korrespondenzSprache",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    sprache: Optional[SprachCode] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    mut_datum: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "mutDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    forcierung: Optional[Forciert] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    werbung: Optional[Werbung] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    werbung_bestaetigung: Optional[WerbungBestaetigung] = field(
        default=None,
        metadata={
            "name": "werbungBestaetigung",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
    version_partner: Optional[int] = field(
        default=None,
        metadata={
            "name": "versionPartner",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
    version_email: Optional[int] = field(
        default=None,
        metadata={
            "name": "versionEmail",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )

    @dataclass
    class QualitaetsEigenschaft:
        """
        :ivar qualitaets_eigenschaft_code:
        :ivar qualitaets_wert: @Deprecated will be removed in NOVA 15.
        :ivar mut_datum:
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
        mut_datum: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "mutDatum",
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
                "required": True,
            }
        )
