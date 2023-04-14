from dataclasses import dataclass, field
from typing import List, Optional
from nova.geld_betrag import GeldBetrag
from nova.leistung_erstattungs_request import LeistungErstattungsRequest
from nova.savangebots_request import SavangebotsRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class ErstattungsAngebotsRequest(SavangebotsRequest):
    """Eine ErstattungsAngebotsanfrage ist eine spezielle Art einer
    SAVAngebotsanfrage.

    Sie wird verwendet, wenn eine bereits verkaufte Leistung erstattet
    werden soll. Siehe auch SAVAngebotsAnfrage.

    :ivar selbst_behalt:
    :ivar zu_erstattende_leistung:
    :ivar selbst_behalt_empfaenger: Partner-Code des Selbstbehalt-
        Empfänger (sofern abweichend von Vermittler)
    """
    selbst_behalt: Optional[GeldBetrag] = field(
        default=None,
        metadata={
            "name": "selbstBehalt",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zu_erstattende_leistung: List[LeistungErstattungsRequest] = field(
        default_factory=list,
        metadata={
            "name": "zuErstattendeLeistung",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_occurs": 1,
        }
    )
    selbst_behalt_empfaenger: Optional[int] = field(
        default=None,
        metadata={
            "name": "selbstBehaltEmpfaenger",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "max_inclusive": 99999,
        }
    )
