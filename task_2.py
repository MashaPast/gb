import xml.etree.ElementTree as ET
import requests
from requests import utils
import ast


def currency_rates(val):
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(r.headers)
    content = r.content.decode(encoding=encodings)

    tree = ET.fromstring(content)
    xml_dict = {}
    for el in tree:
        children = list(el)
        xml_dict[children[1].text.lower()] = ast.literal_eval(children[4].text.replace(',', '.'))
    try:
        return xml_dict[val.lower()]
    except KeyError:
        return None


