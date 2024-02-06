
from nova.vertriebs_service_port_type_soapv14_liefere_belege_fuer_angebot_input import VertriebsServicePortTypeSoapv14LiefereBelegeFuerAngebotInput
from nova.vertriebs_service_port_type_soapv14_liefere_belege_fuer_angebot_output import VertriebsServicePortTypeSoapv14LiefereBelegeFuerAngebotOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14LiefereBelegeFuerAngebot:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/liefereBelegeFuerAngebot"
    input = VertriebsServicePortTypeSoapv14LiefereBelegeFuerAngebotInput
    output = VertriebsServicePortTypeSoapv14LiefereBelegeFuerAngebotOutput
