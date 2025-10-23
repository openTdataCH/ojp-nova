
from nova.vertriebs_service_port_type_soapv14_suche_leistungen_input import VertriebsServicePortTypeSoapv14SucheLeistungenInput
from nova.vertriebs_service_port_type_soapv14_suche_leistungen_output import VertriebsServicePortTypeSoapv14SucheLeistungenOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14SucheLeistungen:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/sucheLeistungen"
    input = VertriebsServicePortTypeSoapv14SucheLeistungenInput
    output = VertriebsServicePortTypeSoapv14SucheLeistungenOutput
