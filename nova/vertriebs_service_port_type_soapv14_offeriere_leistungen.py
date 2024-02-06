
from nova.vertriebs_service_port_type_soapv14_offeriere_leistungen_input import VertriebsServicePortTypeSoapv14OfferiereLeistungenInput
from nova.vertriebs_service_port_type_soapv14_offeriere_leistungen_output import VertriebsServicePortTypeSoapv14OfferiereLeistungenOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14OfferiereLeistungen:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/offeriereLeistungen"
    input = VertriebsServicePortTypeSoapv14OfferiereLeistungenInput
    output = VertriebsServicePortTypeSoapv14OfferiereLeistungenOutput
