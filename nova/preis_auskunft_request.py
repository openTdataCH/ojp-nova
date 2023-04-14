from dataclasses import dataclass, field
from typing import List, Optional
from nova.angebots_filter import AngebotsFilter
from nova.client_identifier import ClientIdentifier
from nova.correlation_kontext import CorrelationKontext
from nova.reisenden_info_preis_auskunft import ReisendenInfoPreisAuskunft
from nova.time_shift import TimeShift

__NAMESPACE__ = "http://nova.voev.ch/services/v14/preisauskunft"


@dataclass
class PreisAuskunftRequest:
    """
    abstrakte Basisklasse für ProduktPreisAuskunft und VerbindungPreisAuskunft.
    """
    client_identifier: Optional[ClientIdentifier] = field(
        default=None,
        metadata={
            "name": "clientIdentifier",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
    correlation_kontext: Optional[CorrelationKontext] = field(
        default=None,
        metadata={
            "name": "correlationKontext",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
    time_shift: Optional[TimeShift] = field(
        default=None,
        metadata={
            "name": "timeShift",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
        }
    )
    angebots_filter: List[AngebotsFilter] = field(
        default_factory=list,
        metadata={
            "name": "angebotsFilter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "min_occurs": 1,
        }
    )
    reisender: List[ReisendenInfoPreisAuskunft] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "min_occurs": 1,
        }
    )
    kunden_segmente_gruppieren: Optional[bool] = field(
        default=None,
        metadata={
            "name": "kundenSegmenteGruppieren",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/preisauskunft",
            "required": True,
        }
    )
