
from nova.vertriebs_service_port_type_soapv14_erstelle_tarif_weg_kombinations_angebot_input import VertriebsServicePortTypeSoapv14ErstelleTarifWegKombinationsAngebotInput
from nova.vertriebs_service_port_type_soapv14_erstelle_tarif_weg_kombinations_angebot_output import VertriebsServicePortTypeSoapv14ErstelleTarifWegKombinationsAngebotOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14ErstelleTarifWegKombinationsAngebot:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/erstelleTarifWegKombinationsAngebot"
    input = VertriebsServicePortTypeSoapv14ErstelleTarifWegKombinationsAngebotInput
    output = VertriebsServicePortTypeSoapv14ErstelleTarifWegKombinationsAngebotOutput
