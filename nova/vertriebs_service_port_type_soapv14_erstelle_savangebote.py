
from nova.vertriebs_service_port_type_soapv14_erstelle_savangebote_input import VertriebsServicePortTypeSoapv14ErstelleSavangeboteInput
from nova.vertriebs_service_port_type_soapv14_erstelle_savangebote_output import VertriebsServicePortTypeSoapv14ErstelleSavangeboteOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14ErstelleSavangebote:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/erstelleSAVAngebote"
    input = VertriebsServicePortTypeSoapv14ErstelleSavangeboteInput
    output = VertriebsServicePortTypeSoapv14ErstelleSavangeboteOutput
