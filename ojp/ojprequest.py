from dataclasses import dataclass
from ojp.ojprequest_structure import OjprequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class Ojprequest(OjprequestStructure):
    """OJP Request - Groups individual functional requests."""
    class Meta:
        name = "OJPRequest"
        namespace = "http://www.siri.org.uk/siri"
