from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class AutomatischeValidierungen:
    """
    Beschreibt die Validierungen, die im Rahmen des Konfidenzprofils automatisch
    durch NOVAGP vorgenommen werden.

    :ivar kuba_check: Gibt an, ob für dieses Konfidenzprofil KUBA-
        Prüfungen der Partnerdaten durchgeführt werden. Dies führt NICHT
        automatisch dazu, dass der Partner in KUBA gespeichert wird.
        Dazu muss zusätzlich das Flag kubaStore gesetzt werden.
    :ivar festnetz_check: Gibt an, ob für dieses Konfidenzprofil eine
        strukturelle Prüfung der Festnetz-Telefonnummer durchgeführt
        wird.
    :ivar mobile_check: Gibt an, ob für dieses Konfidenzprofil eine
        strukturelle Prüfung der Mobile-Telefonnummer durchgeführt wird.
    :ivar email_check: Gibt an, ob für dieses Konfidenzprofil eine
        syntaktische Prüfung der E-Mail-Adresse durchgeführt wird.
    :ivar adress_check: Gibt an, ob für dieses Konfidenzprofil eine
        syntaktische Prüfung der Adresse durchgeführt wird (z.B. Länge
        PLZ entspricht den Anforderungen für das Land).
    :ivar geburts_datum_validiert_check: Gibt an, ob für dieses
        Konfidenzprofil geprüft wird, dass das Geburtsdatum validiert
        ist.
    :ivar dubletten_check: Gibt an, ob für dieses Konfidenzprofil eine
        Dublettenprüfung durchgeführt wird.
    """
    kuba_check: Optional[bool] = field(
        default=None,
        metadata={
            "name": "kubaCheck",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
    festnetz_check: Optional[bool] = field(
        default=None,
        metadata={
            "name": "festnetzCheck",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
    mobile_check: Optional[bool] = field(
        default=None,
        metadata={
            "name": "mobileCheck",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
    email_check: Optional[bool] = field(
        default=None,
        metadata={
            "name": "emailCheck",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
    adress_check: Optional[bool] = field(
        default=None,
        metadata={
            "name": "adressCheck",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
    geburts_datum_validiert_check: Optional[bool] = field(
        default=None,
        metadata={
            "name": "geburtsDatumValidiertCheck",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "required": True,
        }
    )
    dubletten_check: Optional[bool] = field(
        default=None,
        metadata={
            "name": "dublettenCheck",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
        }
    )
