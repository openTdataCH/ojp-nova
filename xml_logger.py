#!/usr/bin/env python3

import pathlib

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from configuration import XML_LOG_ENABLED, XML_LOG_DIR


def enabled() -> str:
    ''' Evaluates if this logger is enabled.'''
    return XML_LOG_ENABLED


# Make sure the path exists
if enabled():
    pathlib.Path(XML_LOG_DIR).mkdir(parents=True, exist_ok=True)


def path(filename) -> str:
    ''' Returns the path of a generated file for xml file logging.'''

    return XML_LOG_DIR + '/' + filename


def log_serialized(filename, xml):
    ''' Writes the serialized xml to file if the xml logger is enabled.'''
    if enabled():
        open(path(filename), 'w', encoding='utf-8').write(xml)


def log_object_as_xml(filename, obj):
    ''' Serializes the object to XML and writes the rendered xml to file if the logger is enabled. '''
    serializer_config = SerializerConfig(ignore_default_attributes=True, pretty_print=True)
    serializer = XmlSerializer(serializer_config)
    xml = serializer.render(obj)
    log_serialized(filename, xml)
