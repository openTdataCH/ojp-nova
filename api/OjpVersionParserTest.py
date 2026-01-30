import logging
import unittest

from api.OjpVersionParser import OjpVersionParser
from api.errors.InvalidOjpRequestError import InvalidOjpRequestError


class OjpVersionParserTest(unittest.TestCase):

    logger = logging.getLogger(__name__)

    def test_ojp1_WHEN_parse_EXPECT_1(self):
        version_parser = OjpVersionParser()
        payload = '<OJP version="1.0"></OJP>'
        version = version_parser.parse_version(payload)
        self.assertEqual(version, '1.0')

    def test_ojp2_WHEN_parse_EXPECT_2(self):
        version_parser = OjpVersionParser()
        payload = '<OJP version="2.0"></OJP>'
        version = version_parser.parse_version(payload)
        self.assertEqual(version, '2.0')

    def test_missing_version_WHEN_parse_EXPECT_failure(self):
        version_parser = OjpVersionParser()
        payload = '<OJP></OJP>'
        with self.assertRaises(InvalidOjpRequestError):
            version_parser.parse_version(payload)

    def test_missing_ojp_element_WHEN_parse_EXPECT_failure(self):
        version_parser = OjpVersionParser()
        payload = '<TEST></TEST>'
        with self.assertRaises(InvalidOjpRequestError):
            version_parser.parse_version(payload)

    def test_no_xml_WHEN_parse_EXPECT_failure(self):
        version_parser = OjpVersionParser()
        payload = 'Test'
        with self.assertRaises(InvalidOjpRequestError):
            version_parser.parse_version(payload)

if __name__ == '__main__':
    unittest.main()