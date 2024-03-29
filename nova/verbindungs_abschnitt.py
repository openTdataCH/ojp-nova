from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from nova.befoerderungs_einschraenkung import BefoerderungsEinschraenkung
from nova.reservations_pflicht import ReservationsPflicht
from nova.verkehrs_mittel_gattung import VerkehrsMittelGattung

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class VerbindungsAbschnitt:
    """
    :ivar befoerderungs_einschraenkung:
    :ivar reservations_pflicht:
    :ivar verkehrs_mittel:
    :ivar id: legId generiert von NOVA
    :ivar index: in der AngebotsAnfrage angegebener
        verbindungsAbschnittsIndex
    :ivar abgang:
    :ivar bestimmung:
    :ivar abfahrts_zeit:
    :ivar ankunfts_zeit:
    :ivar verwaltungs_code:
    """
    befoerderungs_einschraenkung: List[BefoerderungsEinschraenkung] = field(
        default_factory=list,
        metadata={
            "name": "befoerderungsEinschraenkung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    reservations_pflicht: List[ReservationsPflicht] = field(
        default_factory=list,
        metadata={
            "name": "reservationsPflicht",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    verkehrs_mittel: Optional[VerkehrsMittelGattung] = field(
        default=None,
        metadata={
            "name": "verkehrsMittel",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
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
    verwaltungs_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "verwaltungsCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
