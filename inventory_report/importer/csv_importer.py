import csv
from .importer import Importer


class CsvImporter(Importer):
    def __init__(self):
        pass

    def import_data(path):
        if '.csv' in path:
            data = CsvImporter.read_csv(path)
            return data
        else:
            raise ValueError('Arquivo inválido')

    def read_csv(path):
        with open(path) as file:
            products_list = []
            products = csv.DictReader(file, delimiter=",", quotechar='"')
            products_list = list(products)
        return products_list
