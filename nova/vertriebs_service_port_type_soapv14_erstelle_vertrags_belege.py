
from nova.vertriebs_service_port_type_soapv14_erstelle_vertrags_belege_input import VertriebsServicePortTypeSoapv14ErstelleVertragsBelegeInput
from nova.vertriebs_service_port_type_soapv14_erstelle_vertrags_belege_output import VertriebsServicePortTypeSoapv14ErstelleVertragsBelegeOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14ErstelleVertragsBelege:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/erstelleVertragsBelege"
    input = VertriebsServicePortTypeSoapv14ErstelleVertragsBelegeInput
    output = VertriebsServicePortTypeSoapv14ErstelleVertragsBelegeOutput
