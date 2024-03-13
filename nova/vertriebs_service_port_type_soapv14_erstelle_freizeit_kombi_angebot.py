
from nova.vertriebs_service_port_type_soapv14_erstelle_freizeit_kombi_angebot_input import VertriebsServicePortTypeSoapv14ErstelleFreizeitKombiAngebotInput
from nova.vertriebs_service_port_type_soapv14_erstelle_freizeit_kombi_angebot_output import VertriebsServicePortTypeSoapv14ErstelleFreizeitKombiAngebotOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14ErstelleFreizeitKombiAngebot:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/erstelleFreizeitKombiAngebot"
    input = VertriebsServicePortTypeSoapv14ErstelleFreizeitKombiAngebotInput
    output = VertriebsServicePortTypeSoapv14ErstelleFreizeitKombiAngebotOutput
