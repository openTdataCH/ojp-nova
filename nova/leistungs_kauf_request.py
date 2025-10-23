from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from nova.zahlungs_information_request import ZahlungsInformationRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class LeistungsKaufRequest:
    """
    Eine LeistungsKaufanfrage enthält alle Informationen, die notwendig sind, um
    die entsprechende Leistung kaufen zu können.
    """
    zahlungs_information: List[ZahlungsInformationRequest] = field(
        default_factory=list,
        metadata={
            "name": "zahlungsInformation",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    leistungs_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "leistungsId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "required": True,
            "min_inclusive": 0,
        }
    )
    verkaufs_zeitpunkt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "verkaufsZeitpunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
