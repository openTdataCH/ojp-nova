from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nova.savangebots_request import SavangebotsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class EntschaedigungsAngebotsRequest(SavangebotsRequest):
    """Eine EntschädigungsAngebotsanfrage ist eine spezielle Art einer
    SAVAngebotsanfrage.

    Sie wird verwendet, wenn eine bereits verkaufte Leistung bei
    Verspätungen im öV entschädigt werden soll. Siehe auch
    SAVAngebotsAnfrage.
    """
    zu_entschaedigende_leistung: List[int] = field(
        default_factory=list,
        metadata={
            "name": "zuEntschaedigendeLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
            "min_inclusive": 0,
        }
    )
    verspaetungs_datum: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "verspaetungsDatum",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
    verspaetung_in_minuten: Optional[int] = field(
        default=None,
        metadata={
            "name": "verspaetungInMinuten",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "max_inclusive": 9999,
        }
    )
    min_entschaedigungs_betrag_anwenden: Optional[bool] = field(
        default=None,
        metadata={
            "name": "minEntschaedigungsBetragAnwenden",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
        }
    )
