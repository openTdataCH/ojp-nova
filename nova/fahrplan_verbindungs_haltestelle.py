from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class FahrplanVerbindungsHaltestelle:
    """Die Verbindungshaltestelle ist ein Halt innerhalb eines Verbindungssegments
    zu einer bestimmten Zeit an einem bestimmten Ort. Eine Verbindungshaltestelle
    definiert die Ankunfts- und Abfahrtszeit einer Verbindung an einer bestimmten
    angefahrenen Haltestelle. Mitternachtsüberschreitungen: Eine
    Mitternachtsüberschreitung liegt für ein VerbindungsSegment dann vor, wenn das
    Segment am Tag n startet und am Tag n + 1 endet. Eine
    Mitternachtsüberschreitung kann stattfinden:

    - an einer VerbindungsHaltestelle, wenn die Abfahrtszeit und Ankunftszeit nicht am selben Tag liegen. - zwischen zwei aufeinander folgenden Haltestellen, wenn die Abfahrtszeit an einer Haltestelle nicht am selben Tag liegt wie die Ankunftszeit der folgenden VerbindungsHaltestelle.
    Es gibt Spezialfalle, bei denen für die VerbindungsHaltestelle keine Zeiten vorliegen. z.B. sind für VerbindungsHaltestelle, welche zu einem Verbindungssegment für Fusswege (Gattung = Walk) gehören oder virtuelle Haltestellen repräsentieren.
    """
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
    haltestelle: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
