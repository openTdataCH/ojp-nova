from dataclasses import dataclass, field
from typing import List, Optional
from nova.abstract_leistung import AbstractLeistung
from nova.meldungen import Meldungen
from nova.vertriebs_response import VertriebsResponse

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AngebotsKaufResponse(VertriebsResponse):
    """
    :ivar leistung:
    :ivar fehler: Im Falle von Fehlern bei der Verarbeitung einzelner
        Leistungen werden hier die leistungsbezogenen Fehlermeldungen
        zurückgeliefert. Allgemeine Fehlermeldungen werden auf Top-
        Level-Ebene der AngebotsKaufantwort zurückgeliefert.
    """
    leistung: List[AbstractLeistung] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    fehler: List["AngebotsKaufResponse.Fehler"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )

    @dataclass
    class Fehler:
        meldungen: Optional[Meldungen] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
            }
        )
        angebots_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "angebotsId",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "length": 37,
                "pattern": r"_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
            }
        )
        externe_leistungs_referenz_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "externeLeistungsReferenzId",
                "type": "Attribute",
                "namespace": "http://nova.voev.ch/services/v14/vertrieb",
                "required": True,
                "min_length": 0,
                "max_length": 50,
            }
        )
