# File structure of the project

| Folder/File                      | Purpose                                                                        |
|----------------------------------|--------------------------------------------------------------------------------|
| /docs                            | document folder                                                                |
| /generated                       | Generated XML during test                                                      |
| /input                           | Input XML for tests . They are all OJPTripRequest (OJP1.0 and OJP2.)           |
| /logs                            | Location of the log file                                                       |
| /nova                            | xsdata generated py-files for the interface to nova based on the NOVA schema   |
| /ojp                             | xsdata generated py-files for the OJP 1.0 XSD                                  |
| /ojp2                            | xsdata generated py-files for the OJP 2.0 XSD                                  |
| /service                         | Contains the information to start the fare service on a service (with readme)  |
| /venv                            | the virtual environment (only local)                                           |
| /xslt                            | OJP 1.0<->2.0 XSLT (deprecated)                                                |
| configuration.py                 | The whole configuration                                                        |
| extract_fare_products.py         | Extract fare products from the Stammdaten file (don't use)                     |
| fare_products.py                 | Usable version of the fare_products (extracted)                                |
| local_configration.py            | The detailed configuration with secrets.                                       |
| logger                           | The log files                                                                  |
| map_nova_to_ojpX.py              | Mapping between Nova and OJP 1.0 and OJP 2.0 (two different files              |
| map_ojpX_to_nova.py              | Mapping from OJP 1.0 and OJP 2.0 to Nova (two different files)                 |
| map ojpX_to_ojpX.py              | Mapping between OJP (Trip -> Fare) one for OJP 1.0 and one for OJP 2.0         |
| publicode.yml                    | YAML about the project for the harvesting                                      |
| README.md                        | The readme file                                                                |                                           |
| requirements.txt                 | Fetching the necessary libraries                                               |
| server.py  and server_ojp2       | the service                                                                    |
| support.py                       |                                                                                |
| xslt_transform.py                | the code to do the xslt-transform between OJP 1.0 and OJP 2.0 (deprecated)     |
| test_client and test_client_ojp2 |                                                                                |
| test_create_ojpX_request.py      | Code to generate very simple OJPTripRequests (better to use the ones in inputs |
| test_network_flow.py             | The program uses the input files (activated through configuration.py)          |      |
| test_nova_r_r.py                 |                                                                                |
| tests_pr_r_request_nova.py       | Experimental P&R download                                                      |
| tet_stammdaten_request_nova.py   | Experimantal Stammdaten Request                                                |
