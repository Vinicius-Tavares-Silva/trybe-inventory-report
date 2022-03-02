import json
from .importer import Importer


class JsonImporter(Importer):
    def __init__(self):
        pass

    def import_data(path):
        if '.json' in path:
            data = JsonImporter.read_json(path)
            return data
        else:
            raise ValueError('Arquivo inválido')

    def read_json(path):
        with open(path) as file:
            products_list = []
            products_list = json.load(file)
        return products_list
