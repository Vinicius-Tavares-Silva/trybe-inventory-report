from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self):
        pass

    def generate(data):
        company_list = [
            item['nome_da_empresa'] for item in data
        ]
        unique_company_list = list(set(company_list))
        unique_company_list = sorted(
            unique_company_list,
            key=lambda company: company[3]
        )
        str = 'Produtos estocados por empresa: \n'
        for company in unique_company_list:
            str = f'{str}- {company}: 'f'{company_list.count(company)}\n'
        return (
            f'{SimpleReport.generate(data)}\n'
            f'{str}'
        )