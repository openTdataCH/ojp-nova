from dataclasses import dataclass

from ojp2.ojprequest_structure import OjprequestStructure

__NAMESPACE__ = "http://www.vdv.de/ojp"


@dataclass
class Ojprequest(OjprequestStructure):
    """OJP Request - Groups individual functional requests."""

    class Meta:
        name = "OJPRequest"
        namespace = "http://www.vdv.de/ojp"
