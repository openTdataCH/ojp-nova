
from nova.vertriebs_service_port_type_soapv14_erstelle_belege_input import VertriebsServicePortTypeSoapv14ErstelleBelegeInput
from nova.vertriebs_service_port_type_soapv14_erstelle_belege_output import VertriebsServicePortTypeSoapv14ErstelleBelegeOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14ErstelleBelege:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/erstelleBelege"
    input = VertriebsServicePortTypeSoapv14ErstelleBelegeInput
    output = VertriebsServicePortTypeSoapv14ErstelleBelegeOutput
