import xml.etree.ElementTree as ET
import os
from configuration import GENERATED_DIR

current_directory = os.getcwd()
# Parse the XML file
tree = ET.parse(os.path.join(current_directory, GENERATED_DIR, 'nova_stammdaten.xml'))
root = tree.getroot()

# Initialize the dictionary
products = {}

# Extract the desired information
for product_info in root.findall('.//{http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten}produktInfo'):
    product_nummer = product_info.attrib['{http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten}produktNummer']
    bez = product_info.find('{http://nova.voev.ch/services/v14/vertrieb/vertriebsstammdaten}produktBezeichnung')
    if bez is None:
        print(product_nummer)
        # Add the extracted data to the dictionary
        products[product_nummer] = product_nummer

    else:
        product_bezeichnung=bez.attrib['{http://nova.voev.ch/services/v14/base}defaultWert']
        # Add the extracted data to the dictionary
        products[product_nummer] = product_bezeichnung

# Generate the out.py file
with open(os.path.join(current_directory, GENERATED_DIR, 'out.py'), 'w',encoding='utf-8') as f:
    f.write('products = {}\n'.format(products))