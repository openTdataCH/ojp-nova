
from nova.vertriebs_service_port_type_soapv14_erstelle_angebote_input import VertriebsServicePortTypeSoapv14ErstelleAngeboteInput
from nova.vertriebs_service_port_type_soapv14_erstelle_angebote_output import VertriebsServicePortTypeSoapv14ErstelleAngeboteOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14ErstelleAngebote:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/erstelleAngebote"
    input = VertriebsServicePortTypeSoapv14ErstelleAngeboteInput
    output = VertriebsServicePortTypeSoapv14ErstelleAngeboteOutput
