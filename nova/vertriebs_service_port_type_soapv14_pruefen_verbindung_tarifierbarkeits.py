
from nova.vertriebs_service_port_type_soapv14_pruefen_verbindung_tarifierbarkeits_input import VertriebsServicePortTypeSoapv14PruefenVerbindungTarifierbarkeitsInput
from nova.vertriebs_service_port_type_soapv14_pruefen_verbindung_tarifierbarkeits_output import VertriebsServicePortTypeSoapv14PruefenVerbindungTarifierbarkeitsOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/vertrieb"


class VertriebsServicePortTypeSoapv14PruefenVerbindungTarifierbarkeits:
    style = "document"
    location = "http://nova.voev.ch/novaan/vertrieb/public/v14/VertriebsService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "http://nova.voev.ch/services/v14/vertrieb/pruefenVerbindungTarifierbarkeits"
    input = VertriebsServicePortTypeSoapv14PruefenVerbindungTarifierbarkeitsInput
    output = VertriebsServicePortTypeSoapv14PruefenVerbindungTarifierbarkeitsOutput
