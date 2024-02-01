from dataclasses import dataclass, field
from typing import List, Optional
from nova.localized_string import LocalizedString

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten"


@dataclass
class Partner2:
    """
    :ivar druck_bezeichnung:
    :ivar druck_kuerzel:
    :ivar screen_bezeichnung:
    :ivar partner_rolle: Beschreibt die Rollen, die ein Partner besitzt.
    :ivar partner_code:
    :ivar partner_kuerzel:
    :ivar kontakt_email: Kontakt-E-Mail-Adresse des Partners.
    :ivar bezeichnung:
    :ivar website_url: URL zur Website des Partners.
    :ivar logo_url: URL zu einem Image des Partner-Logos (PNG, JPG, GIF,
        SVG)
    """
    class Meta:
        name = "Partner"

    druck_bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "druckBezeichnung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    druck_kuerzel: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "druckKuerzel",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    screen_bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "name": "screenBezeichnung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
        }
    )
    partner_rolle: List[str] = field(
        default_factory=list,
        metadata={
            "name": "partnerRolle",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 0,
            "max_length": 200,
        }
    )
    partner_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "partnerCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "max_inclusive": 99999,
        }
    )
    partner_kuerzel: Optional[str] = field(
        default=None,
        metadata={
            "name": "partnerKuerzel",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    kontakt_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "kontaktEmail",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "min_length": 0,
            "max_length": 255,
        }
    )
    bezeichnung: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "required": True,
            "min_length": 0,
            "max_length": 200,
        }
    )
    website_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "websiteUrl",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "max_length": 2048,
        }
    )
    logo_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "logoUrl",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten",
            "max_length": 2048,
        }
    )
