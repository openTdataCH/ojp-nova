from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from nova.leistung_verkaufs_parameter_type import LeistungVerkaufsParameterType
from nova.zahlungs_information_request import ZahlungsInformationRequest

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


@dataclass
class AngebotsKaufRequestParam:
    """
    :ivar verkaufs_parameter:
    :ivar zahlungs_information:
    :ivar angebots_id: Angebots-ID, die bei erstelleAngebote geliefert
        wurde.
    :ivar leistungs_referenz:
    :ivar externe_leistungs_referenz_id: Für den ClientIdentifier
        (Vermittler) eindeutige ID der verkauften Leistung zur
        angebotsId. Dient der Zuordnung im Fehlerfall und bei
        wiederholtem Aufruf.
    :ivar verkaufs_zeitpunkt: Optionale Angabe des Verkaufszeitpunkts.
        Wird dann so in die erstellte NOVA Leistung übernommen.
    :ivar externe_reisenden_referenz_id:
    """
    verkaufs_parameter: List[LeistungVerkaufsParameterType] = field(
        default_factory=list,
        metadata={
            "name": "verkaufsParameter",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    zahlungs_information: List[ZahlungsInformationRequest] = field(
        default_factory=list,
        metadata={
            "name": "zahlungsInformation",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
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
    leistungs_referenz: Optional[str] = field(
        default=None,
        metadata={
            "name": "leistungsReferenz",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
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
    verkaufs_zeitpunkt: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "verkaufsZeitpunkt",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
        }
    )
    externe_reisenden_referenz_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "externeReisendenReferenzId",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertrieb",
            "min_length": 0,
            "max_length": 50,
        }
    )
