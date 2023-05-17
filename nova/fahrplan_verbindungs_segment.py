from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from nova.verkehrs_mittel_gattung import VerkehrsMittelGattung
from nova.zwischen_halt_context_trip_context import ZwischenHaltContextTripContext

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class FahrplanVerbindungsSegment:
    """Ein Verbindungssegment entspricht einer (Teil)-Verbindung, auf welcher die
    Verwaltung, Gattung (resp.

    Nummer) gleich bleibt. Typischerweise werden beim Umsteigen auf ein
    anderes VerkehrsMittel mehrere Verbindungssegmente benötigt.

    :ivar verkehrs_mittel:
    :ivar zwischen_halt:
    :ivar zwischen_halt_context:
    :ivar einstieg: Für das erste Segment immer gefüllt.
    :ivar ausstieg: Für das letzte Segment immer gefüllt.
    :ivar verwaltungs_code:
    :ivar info_plus_tarif_code:
    :ivar abfahrts_zeit: Auf dem ersten FahrplanverbindungsSegment muss
        eine Abfahrtszeit gesetzt sein.
    :ivar ankunfts_zeit: Auf dem letzten FahrplanverbindungsSegment muss
        eine Ankunftszeit gesetzt sein.
    """
    verkehrs_mittel: Optional[VerkehrsMittelGattung] = field(
        default=None,
        metadata={
            "name": "verkehrsMittel",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    zwischen_halt: List[int] = field(
        default_factory=list,
        metadata={
            "name": "zwischenHalt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    zwischen_halt_context: List["FahrplanVerbindungsSegment.ZwischenHaltContext"] = field(
        default_factory=list,
        metadata={
            "name": "zwischenHaltContext",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    einstieg: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
        }
    )
    ausstieg: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_inclusive": 0,
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
    info_plus_tarif_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "infoPlusTarifCode",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    abfahrts_zeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "abfahrtsZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    ankunfts_zeit: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ankunftsZeit",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class ZwischenHaltContext:
        uic_code: Optional[int] = field(
            default=None,
            metadata={
                "name": "uicCode",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_inclusive": 0,
            }
        )
        trip_context: Optional[ZwischenHaltContextTripContext] = field(
            default=None,
            metadata={
                "name": "tripContext",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
