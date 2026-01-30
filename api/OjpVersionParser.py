from xml.etree import ElementTree

from api.errors.InvalidOjpRequestError import InvalidOjpRequestError


class OjpVersionParser:
    chunk_size = 8192  # ausreichend gross, um alle Root-Attribute zu erwischen
    root_element_name = "OJP"

    def parse_version(self, xml_content: str) -> str:
        """
        Reads until first start tag and gets the value of the 'version' attribute
        of the OJP root element.

        Raises:
            InvalidOjpRequestError upon invalid XML, unexcepted root element or missing version attribute.
        """

        parser = ElementTree.XMLPullParser(events=('start',))
        pos = 0

        while True:
            if pos >= len(xml_content):
                # end of the document reached without having seen the root element
                try:
                    parser.close()
                except ElementTree.ParseError as e:
                    raise InvalidOjpRequestError(f"Invalid XML: {e}") from e
                raise InvalidOjpRequestError("Root element not found.")

            parser.feed(xml_content[pos:pos + self.chunk_size])
            pos += self.chunk_size

            for event, elem in parser.read_events():
                # first start event is the root
                tag = elem.tag
                local = tag.split('}', 1)[1] if tag.startswith('{') else tag

                if local != self.root_element_name:
                    raise InvalidOjpRequestError(f"Root-Element ist '{local}', erwartet '{self.root_element_name}'")

                ver = elem.get("version")
                if ver is None or ver.strip() == "":
                    raise InvalidOjpRequestError(f"'{self.root_element_name}'-Element hat kein 'version'-Attribut.")

                return ver.strip()
