# OJPFare service for Switzerland
This repository contains the necessary code integrate OJP into the NOVA Preisauskunft in Switzerland
.
## Installation

### Initial steps
1. Check out the code
2. Create a pycharm project from it

Necessary libraries are named in requirements.txt
```
$ python3 -m pip install -r requirements.txt
```

### generation of code from the XSD
With xsdata we create ojp classes that use the schema and are then used within the project.
You need an xsdata for OJP 1.0:
```
xsdata -p ojp -ss clusters path-to-ojp.xsd
```

You need also a configuration for OJP 2.0:
```
xsdata -p ojp2 -ss clusters path-to-ojp.xsd
```

This is not neede for nova as the necessary xsdata objects are already created in the folder nova.

### Configuration
The main configuration is stored in configuration.py. However, you need additional information to make this work.
We suggest to use local_configuration.py (is omitted through .gitignore).

If you need some configuration it may be discussed. Contact opendata@sbb.ch, if necessary. Be aware, that the NOVA product team needs to agree. However, the access is and will remain limited.
Relevant element that need to be filled:
```
NOVA_URL_TOKEN = ""
NOVA_CLIENT_ID = ''
NOVA_CLIENT_SECRET = ''
NOVA_URL_API = ""
OJP_URL_API = "https://api.opentransportdata.swiss/ojp2020"
OJP_TOKEN = ''
OJP2_URL_API = "https://api.opentransportdata.swiss/ojp20"
OJP2_TOKEN = ''
xxx
```

### Testing the configuration
You can test the configuration with test_network_flow.py.

This will run a local run through (see section on testing).

The following should happen 
1. client: Builds an `OJPTripRequest` from "Bern" to "Zürich" with departure time now
2. client: The `OJPTripDelivery` from OJP is obtained
3. client: From the result an `OJPFareRequest` ist constructed
4. client: the OJPFareRequest ist sent to the server
5. server: Transforms the `OJPFareRequest` into a NOVA Preisauskunft request
6. server: Process the result from NOVA, build an `OJPFareDelivery` and send it to the client
7. client: Show the result
8. 
Everything is written to xml files for inspection  in the folder `generated`

## Starting the server
run `server.py `
starts a server on: http://127.0.0.1:8000 

### First connection test
run `test_client.py` 
This will result in a TripRequest/TripDelivery to the OJP service. 

### Create Python service
see [service](./service/)


## How the actual service is built

The service is stateless and can connect to the Swiss OJP v1 service, the Swiss OJP v2 service and the NOVA system.
For simplicity we don't distinguish OJP v1 and OJP v2 in the diagrams.

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

# Handling OJP 1.0 and OJP 2.0
- Originally OJPFare was built for OJP 1.0
- With service_ojp2.py we now have also a service for OJP 2.0.
- test_network_flow.py can process both (it uses the version="1.0" or version="2.0" attribute of the OJP element to decide, which path to use.
- test_client_ojp2.py is the test client for OJP 2.0 services.

A lot was done with a duplification of files/functions:

| OJP 1.0                  | OJP 2.0 | Explanation                   |
|--------------------------|---------|-------------------------------|
| server.py                |server_ojp2.py| test simpler server           |
| test_client.py           |test_client_ojp2.py| The client to test the server |
| test_create_ojp_request.py |test_create_ojp2_request.py| Creates valid requests|
|map_ojp_to_ojp.py |map_ojp2_to_ojp2.py |Functions to map trip delivery to fare request |
|map_ojp_to_nova.py |map_ojp2_to_nova.py |Functions to map the fare request to a nova request|
|map_nova_to_ojp.py |map_nova_to_ojp2.py|Functions to map the nova response to an OJP fare delivery|

There was also an idea to do it with xslt (OJP 2.0 -> OJP 1.0). For testing purposes it currently was easier to duplicate the programs.

# The special case of tariff codes
Tariff codes are used in some very special cases. They are transported in the text or user_text of the Attribute element.
They are used as "TC-<the value>". The value needs to be transferred to nova for a correct calculation. This is done in the new code.

# Usage notes
- The TripResult used in the OJP fare service should not be based on short-term real-time information. So the TripRequest should usually contain a UseRealtime set to false.
- The price is only in one direction. If the full price in both directions is needed and artificial trip must be constructed, that contains all necessary legs in both direction (and works from the time view): Search A to B, some delay, search B to A, concatenate the trips into one. This IS necessary as sometimes the trip in  both direction is cheaper than two single trips.
- We base on the commercial stops (as BPUIC). The calls are more and more based on the SLOID. It is important only provide the commerical stops to NOVA. In some cases the commercial stop is no longer directly based on the other one (e.g. Europaplatz). The right one must be obtained from the PlaceContext (done in `sloid2didok` function).


# Testing
In the folder `input` there are possible xml files. Some work, some are problematic
The selection of files to use in `test_network_flow.py` is done by `test_configuration.py` which basically contains an array
of the files to use. `test_configuration.py` contains the explanaition on what works and what not.

Be aware: For some discount tickets the trip needs to be several days in the future. Currently this needs to be set manually in the respective 
request file in `input`. We don't use the `<ojp:DepArrTime>2025-10-10T15:30:40</ojp:DepArrTime>` in many cases, as trips in the past don't have prives.
If it is omitted, then `now` is used. but we keep it in the files commented out, so that you just can put in the time.


# Changelog

## 1.3 
- Better error handling

## 1.2 prepared for dockerization
- Make sure that we can run this in our new environment.

## 1.1 Bug fixes, better documentation, better testing
- OJP 2.0 support
- Handling of tariff codes
- Improved mypy, black and the like (better code)
- More examples
- Fixed some bugs in testing part

## 1.0
Basic version running with everything needed for OJP 1.0

## Roadmap
Currently no further roadmap defined

# License 
The code is made available as MIT license. The generated code in the "nova" folder based on the WSDL is property of SBB (www.sbb.ch) and not part of the license.

# Assistance
If you need something about this project, just use the issue tracker: https://github.com/openTdataCH/ojp-nova/issues or contact us at opendata@sbb.ch.
