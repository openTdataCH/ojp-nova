# OJPFARE 2 NOVA
This repository contains the necessary code integrate OJP into the NOVA Preisauskunft.

## Requirements
1. Check out the code
2. Create a pycharm project from it

Necessary libraries are named in requirements.txt.

## generation of code from the XSD

```
xsdata -p ojp -ss clusters path-to-ojp.xsd
```
## Configuration
The repository is missing the relevant configuration.
The configuration is only handed out, when necessary. Contact opendata@sbb.ch, if necessary. However, the access is and will remain limited.

Relevant fields:
```
NOVA_URL_TOKEN = ""
NOVA_CLIENT_ID = ''
NOVA_CLIENT_SECRET = ''
NOVA_URL_API = ""
OJP_URL_API = "https://api.opentransportdata.swiss/ojp2020"
OJP_TOKEN = ''
```
## Starting the server
run server.py 
starts a server on: http://127.0.0.1:8000 

## First connection test
run test_client.py 
This will result in a TripRequest/TripDelivery to the OJP service. 

## Create Python service
see [service](./service/)

## Processing the whole flow (as an example)
run network_flow.py 
The following should happen 
1. client: Builds an OJPTripRequest from "Bern" to "Zürich" with departure time now
2. client: The OJPTripDelivery from OJP is obtained
3. client: From the result an OJPFareRequest ist constructed
4. client: the OJPFareRequest ist sent to the server
5. server: Transforms the OJPFareRequest into a NOVA Preisauskunft requdst
6. server: Process the result from NOVA, build an OJPFareDelivery and send it to the client
7. client: Show the result

Everything is written to xml files for inspection

## How the actual service is built
### Component diagram
![image](https://github.com/openTdataCH/ojp-nova/assets/24227470/b20eb8c9-6c94-4e77-8f5e-e870d59b16cf)
```
@startuml
() OJP - [tyk API manager]
[tyk API manager] - () OJP_int
node "The new service" {
  [https proxy] -   [OJPFare2Nova]
}
() OJP_int - [https proxy]
[OJPFare2Nova] - () OJPTrip
() OJPTrip - ["OJP Service (opentransportdata.swiss)"]
[OJPFare2Nova] -- () "Preisauskunft"
() "Preisauskunft" - [Nova service]
@enduml
```


## Sequence diagram

![image](https://github.com/openTdataCH/ojp-nova/assets/24227470/ffc5e9be-bac9-4ca3-8da2-1dbd16516b02)

```
@startuml
Client -> "tyk": OJPTripRequest
tyk -> "https proxy": OJPTripRequest
"https proxy" -> OJPFare2Nova: OJPTripRequest
OJPFare2Nova -> "OJP Service": OJPTripRequest
"OJP Service" --> OJPFare2Nova: OJPTripDelivery
OJPFare2Nova --> "https proxy": OJPTripDelivery
"https proxy" --> tyk: OJPTripDelivery
tyk --> Client: OJPTripDelivery
Client -> Client: "Wrap trips into OJPFare Request"
Client -> tyk: OJPFareRequest
tyk -> "https proxy": OJPFareRequest
"https proxy" -> OJPFare2Nova: OJPFareRequest
OJPFare2Nova -> OJPFare2Nova: MapOJP2Nova
OJPFare2Nova -> Nova: "Nova Preisauskunft"
Nova --> OJPFare2Nova : "Nova Preisauskunft"
OJPFare2Nova -> OJPFare2Nova: "MapNova2OJP"
OJPFare2Nova --> "https proxy": OJPFareDelivery
"https proxy" --> tyk: OJPFareDelivery
tyk --> Client: OJPFareDelivery
@enduml
```

# Usage notes
* The TripResult used in the OJP fare service should not be based on short-term real-time information. So the TripRequest should usually contain a UseRealtime set to false.
* 
# License 
The code is made available as MIT license. The generated code in the "nova" folder based on the WSDL is property of SBB (www.sbb.ch) and not part of the license.
# Assistance
If you need something about this project, just use the issue tracker: https://github.com/openTdataCH/ojp-nova/issues
