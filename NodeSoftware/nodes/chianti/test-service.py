from lxml import etree
import requests

def check_availability():
    print('Availability schema')
    r1 = requests.get('http://www.ivoa.net/xml/VOSIAvailability/VOSIAvailability-v1.0.xsd')
    print(r1.status_code)
    doc = etree.XML(r1.content)
    schema_root = etree.XML(r1.content)
    schema = etree.XMLSchema(schema_root)
    parser = etree.XMLParser(schema = schema)

    print('Availability')
    r2 = requests.get('http://localhost:8000/tap/availability')
    print(r2.status_code)
    print(r2.encoding)
    print(r2.content)

    doc = etree.fromstring(r2.content, parser)
    print('XML well formed, syntax ok.')


def check_capability():
    print('Capability schema')
    #r1 = requests.get('http://www.ivoa.net/xml/VOSICapabilities/VOSICapabilities-v1.0.xsd')
    r1 = requests.get('http://www.vamdc.org/xml/VAMDC-TAP/v1.0')
    print(r1.status_code)
    doc = etree.XML(r1.content)
    schema_root = etree.XML(r1.content)
    schema = etree.XMLSchema(schema_root)
    parser = etree.XMLParser(schema = schema)

    print('Capability')
    r2 = requests.get('http://localhost:8000/tap/capabilities')
    print(r2.status_code)
    print(r2.encoding)
    print(r2.content)

    doc = etree.fromstring(r2.content, parser)
    print('XML well formed, syntax ok.')


check_availability()
check_capability()
