import csv
import json
import xml.etree.ElementTree as ET
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    def __init__(self):
        pass

    def import_data(path, type):
        if '.csv' in path:
            data = Inventory.read_csv(path)
        elif '.json' in path:
            data = Inventory.read_json(path)
        else:
            data = Inventory.read_xml(path)

        if type == 'simples':
            simple_report = SimpleReport.generate(data)
            return f'{simple_report}'
        elif type == 'completo':
            complete_report = CompleteReport.generate(data)
            return f'{complete_report}'

    def read_csv(path):
        with open(path) as file:
            products_list = []
            products = csv.DictReader(file, delimiter=",", quotechar='"')
            products_list = list(products)
        return products_list

    def read_json(path):
        with open(path) as file:
            products_list = []
            products_list = json.load(file)
        return products_list

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
