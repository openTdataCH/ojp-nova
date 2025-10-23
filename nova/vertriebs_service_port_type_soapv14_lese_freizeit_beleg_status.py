
from nova.vertriebs_service_port_type_soapv14_lese_freizeit_beleg_status_input import VertriebsServicePortTypeSoapv14LeseFreizeitBelegStatusInput
from nova.vertriebs_service_port_type_soapv14_lese_freizeit_beleg_status_output import VertriebsServicePortTypeSoapv14LeseFreizeitBelegStatusOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14LeseFreizeitBelegStatus:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/leseFreizeitBelegStatus"
    input = VertriebsServicePortTypeSoapv14LeseFreizeitBelegStatusInput
    output = VertriebsServicePortTypeSoapv14LeseFreizeitBelegStatusOutput
