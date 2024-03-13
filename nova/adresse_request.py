from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://nova.voev.ch/services/v14/geschaeftspartner"


@dataclass
class AdresseRequest:
    """
    :ivar land:
    :ivar ort:
    :ivar plz:
    :ivar adress_zusatz:
    :ivar strasse_hnr: @Deprecated will be removed in NOVA 15, please
        use "streetHousenumber" instead.
    :ivar street_housenumber:
    :ivar postfach:
    :ivar postfach_vorhanden: Flag, das angibt, dass für den Partner ein
        Postfach vorhanden ist, obwohl dieses nicht explizit als
        "postfach" aufgeführt wird.
    """
    land: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 2,
            "max_length": 2,
            "pattern": r"[A-Z]{2}",
        }
    )
    ort: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 30,
        }
    )
    plz: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 15,
        }
    )
    adress_zusatz: Optional[str] = field(
        default=None,
        metadata={
            "name": "adressZusatz",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 30,
        }
    )
    strasse_hnr: Optional[str] = field(
        default=None,
        metadata={
            "name": "strasseHnr",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 30,
        }
    )
    street_housenumber: Optional[str] = field(
        default=None,
        metadata={
            "name": "streetHousenumber",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 60,
        }
    )
    postfach: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "min_length": 0,
            "max_length": 5,
        }
    )
    postfach_vorhanden: Optional[bool] = field(
        default=None,
        metadata={
            "name": "postfachVorhanden",
            "type": "Element",
            "namespace": "http://nova.voev.ch/services/v14/geschaeftspartner",
            "nillable": True,
        }
    )
