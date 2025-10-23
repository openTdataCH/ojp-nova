from dataclasses import dataclass
from ojp.ojpresponse_structure import OjpresponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class Ojpresponse(OjpresponseStructure):
    """OJP Request - Groups individual functional responses."""
    class Meta:
        name = "OJPResponse"
        namespace = "http://www.siri.org.uk/siri"
