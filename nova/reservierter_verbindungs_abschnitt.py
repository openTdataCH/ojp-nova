from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ReservierterVerbindungsAbschnitt:
    verbindungs_abschnitt_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "verbindungsAbschnittId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    abgang: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    bestimmung: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    abfahrts_zeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "abfahrtsZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    ankunfts_zeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ankunftsZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    gattungs_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "gattungsCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    verkehrs_mittel_nummer: Optional[int] = field(
        default=None,
        metadata={
            "name": "verkehrsMittelNummer",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    verwaltungs_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "verwaltungsCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
