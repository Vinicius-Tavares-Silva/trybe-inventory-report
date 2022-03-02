import xml.etree.ElementTree as ET
from .importer import Importer


class XmlImporter(Importer):
    def __init__(self):
        pass

    def import_data(path):
        if '.xml' in path:
            data = XmlImporter.read_xml(path)
            return data
        else:
            raise ValueError('Arquivo inválido')

    def read_xml(path):
        tree = ET.parse(path)
        dataset = tree.getroot()
        tag_array = []
        text_array = []
        products_list = []
        for record in dataset:
            for tag in record:
                tag_array.append(tag.tag)
                text_array.append(tag.text)

            object = dict(zip(tag_array, text_array))
            products_list.append(object)
            tag_array = []
            text_array = []
        return products_list
