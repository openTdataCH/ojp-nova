from dataclasses import dataclass

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertriebsbase"


@dataclass
class EmptyType:
    """
    The empty type, containing neither attributes nor elements, used as Wildcard in
    Taxonomieklassepfad.
    """
