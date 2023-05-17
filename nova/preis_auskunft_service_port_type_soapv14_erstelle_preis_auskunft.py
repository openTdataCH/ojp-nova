
from nova.preis_auskunft_service_port_type_soapv14_erstelle_preis_auskunft_input import PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput
from nova.preis_auskunft_service_port_type_soapv14_erstelle_preis_auskunft_output import PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput

__NAMESPACE__ = "http://nova.voev.ch/services/v14/preisauskunft"


class PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunft:
    style = "document"
    location = "http://nova.voev.ch/novapa/vertrieb/public/v14/PreisAuskunftService"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soap_action = "https://nova.voev.ch/services/v14/preisauskunft/erstellePreisAuskunft"
    input = PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftInput
    output = PreisAuskunftServicePortTypeSoapv14ErstellePreisAuskunftOutput
