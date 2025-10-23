
from nova.vertriebs_service_port_type_soapv14_erstelle_freizeit_belege_input import VertriebsServicePortTypeSoapv14ErstelleFreizeitBelegeInput
from nova.vertriebs_service_port_type_soapv14_erstelle_freizeit_belege_output import VertriebsServicePortTypeSoapv14ErstelleFreizeitBelegeOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14ErstelleFreizeitBelege:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/erstelleFreizeitBelege"
    input = VertriebsServicePortTypeSoapv14ErstelleFreizeitBelegeInput
    output = VertriebsServicePortTypeSoapv14ErstelleFreizeitBelegeOutput
