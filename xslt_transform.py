from lxml import etree

def is_version_2_0(xml_string:str) -> bool:
    #simple test to see if the xml is OJP version 2.0 (or should be)
    # Split the string into lines
    lines = xml_string.splitlines()

    # Check if there are at least two lines
    if len(lines) < 2:
        return False

    # Check the second line for the version
    second_line = lines[1]
    return 'version="2.0"' in second_line
def transform_xml(xml_string, xslt_file):
    try:
        # Parse the XML string
        xml_doc = etree.fromstring(xml_string)

        # Read the XSLT from the file
        with open(xslt_file, 'r') as file:
            xslt_string = file.read()

        # Parse the XSLT string
        xslt_doc = etree.fromstring(xslt_string)

        # Create an XSLT transformer
        transform = etree.XSLT(xslt_doc)

        # Perform the transformation
        result = transform(xml_doc)

        # Return the transformed result as a string
        return str(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None  #TODO
