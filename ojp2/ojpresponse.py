from dataclasses import dataclass

from ojp2.ojpresponse_structure import OjpresponseStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class Ojpresponse(OjpresponseStructure):
    """OJP Request - Groups individual functional responses."""

    class Meta:
        name = "OJPResponse"
        namespace = "http://www.vdv.de/ojp"
