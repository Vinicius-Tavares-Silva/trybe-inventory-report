import csv
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport


class Inventory:
    def __init__(self):
        pass

    def import_data(path, type):
        data = Inventory.read(path)
        if type == 'simples':
            simple_report = SimpleReport.generate(data)
            return f'{simple_report}'
        elif type == 'completo':
            complete_report = CompleteReport.generate(data)
            return f'{complete_report}'

    def read(path):
        with open(path) as file:
            products_list = []
            products = csv.DictReader(file, delimiter=",", quotechar='"')
            products_list = list(products)
        return products_list
