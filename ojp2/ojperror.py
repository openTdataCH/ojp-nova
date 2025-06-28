from dataclasses import dataclass

from ojp2.ojperror_structure import OjperrorStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class Ojperror(OjperrorStructure):
    """Error: All OJP related errors."""

    class Meta:
        name = "OJPError"
        namespace = "http://www.vdv.de/ojp"
