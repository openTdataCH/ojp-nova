from dataclasses import dataclass, field
from typing import List, Optional
from nova.localized_string import LocalizedString
from nova.verkaufs_parameter_wert import VerkaufsParameterWert
from nova.verkaufs_parameter_wert_typ import VerkaufsParameterWertTyp

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class VerkaufsParameterTyp:
    """
    VerkaufsParameterTypen geben dem Leistungsvermittler an, welche Daten für die
    Offerte einer Leistung zwingend anzugeben sind.
    """
    bezeichnung: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    moeglicher_wert: List[VerkaufsParameterWert] = field(
        default_factory=list,
        metadata={
            "name": "moeglicherWert",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    wert: Optional[VerkaufsParameterWert] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
            "min_length": 0,
            "max_length": 50,
        }
    )
    wert_typ: Optional[VerkaufsParameterWertTyp] = field(
        default=None,
        metadata={
            "name": "wertTyp",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
            "required": True,
        }
    )
    format_einschraenkung: Optional[str] = field(
        default=None,
        metadata={
            "name": "formatEinschraenkung",
            "type": "Attribute",
            "namespace": "http://nova.voev.ch/services/v14/vertriebsbase",
        }
    )
