import datetime
import statistics


class SimpleReport:
    def __init__(self):
        pass

    def generate(list):
        sorted_by_manufacturing_date = sorted(
            list,
            key=lambda item:
                SimpleReport.sort_by_date(item, 'data_de_fabricacao'),
            reverse=True
        )
        oldest_date = SimpleReport.get_item(
            sorted_by_manufacturing_date,
            'data_de_fabricacao'
        )

        sorted_by_expiration_date = sorted(
            list,
            key=lambda item:
                SimpleReport.sort_by_date(item, 'data_de_validade')
        )
        newest_date = SimpleReport.get_item(
            sorted_by_expiration_date,
            'data_de_validade'
        )

        company_list = [
            item['nome_da_empresa'] for item in list
        ]
        company = statistics.mode(company_list)

        return (
            f'Data de fabricação mais antiga: {oldest_date}\n'
            f'Data de validade mais próxima: {newest_date}\n'
            f'Empresa com maior quantidade de produtos estocados: {company}\n'
        )

    def sort_by_date(item, key):
        now = datetime.datetime.now()
        d = item[key].split('-')
        date = datetime.datetime(int(d[0]), int(d[1]), int(d[2]))
        date_diff = date - now
        if (int(date_diff.days) > 0):
            return int(date_diff.days)
        return abs(int(date_diff.days))

    def get_item(list, key):
        item = list[0]
        return item[key]
