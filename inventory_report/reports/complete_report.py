import collections
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self):
        pass

    def generate(data):
        company_list = [
            item['nome_da_empresa'] for item in data
        ]
        company_counter = collections.Counter(company_list)
        str = 'Produtos estocados por empresa: \n'
        for company in company_counter:
            str = f'{str}- {company}: 'f'{company_counter[company]}\n'
        return (
            f'{SimpleReport.generate(data)}\n'
            f'{str}'
        )
