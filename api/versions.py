import logging
import unittest
from xml.etree import ElementTree

from .errors import InvalidOjpRequestError


class OjpVersionParser:
    chunk_size = 8192
    root_element_name = "OJP"

    def parse_version(self, xml_content: str) -> str:
        """
        Reads until first start tag and gets the value of the 'version' attribute
        of the OJP root element.

        Raises:
            InvalidOjpRequestError upon invalid XML, unexcepted root element or missing version attribute.
        """

        parser = ElementTree.XMLPullParser(events=("start",))
        pos = 0

        while True:
            if pos >= len(xml_content):
                # end of the document reached without having seen the root element
                try:
                    parser.close()
                except ElementTree.ParseError as e:
                    raise InvalidOjpRequestError(f"Invalid XML: {e}") from e
                raise InvalidOjpRequestError("Root element not found.")

            parser.feed(xml_content[pos : pos + self.chunk_size])
            pos += self.chunk_size

            for event, elem in parser.read_events():
                # first start event is the root
                tag = elem.tag
                local = tag.split("}", 1)[1] if tag.startswith("{") else tag

                if local != self.root_element_name:
                    raise InvalidOjpRequestError(
                        f"Root element is '{local}', expected '{self.root_element_name}'"
                    )

                ver = elem.get("version")
                if ver is None or ver.strip() == "":
                    raise InvalidOjpRequestError(
                        f"'{self.root_element_name}' element has no version attribute."
                    )

                return ver.strip()


class OjpVersionParserTest(unittest.TestCase):
    logger = logging.getLogger(__name__)

    def test_ojp1_WHEN_parse_EXPECT_1(self):
        version_parser = OjpVersionParser()
        payload = '<OJP version="1.0"></OJP>'
        version = version_parser.parse_version(payload)
        self.assertEqual(version, "1.0")

    def test_ojp2_WHEN_parse_EXPECT_2(self):
        version_parser = OjpVersionParser()
        payload = '<OJP version="2.0"></OJP>'
        version = version_parser.parse_version(payload)
        self.assertEqual(version, "2.0")

    def test_missing_version_WHEN_parse_EXPECT_failure(self):
        version_parser = OjpVersionParser()
        payload = "<OJP></OJP>"
        with self.assertRaises(InvalidOjpRequestError):
            version_parser.parse_version(payload)

    def test_missing_ojp_element_WHEN_parse_EXPECT_failure(self):
        version_parser = OjpVersionParser()
        payload = "<TEST></TEST>"
        with self.assertRaises(InvalidOjpRequestError):
            version_parser.parse_version(payload)

    def test_no_xml_WHEN_parse_EXPECT_failure(self):
        version_parser = OjpVersionParser()
        payload = "Test"
        with self.assertRaises(InvalidOjpRequestError):
            version_parser.parse_version(payload)


if __name__ == "__main__":
    unittest.main()
