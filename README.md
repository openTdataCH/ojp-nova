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

## Processing the whole flow
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


## TODO
* Testing and debugging
* wrap the flow in a container to run
* Add some logging/restart check capabilites
* Add heart beat
