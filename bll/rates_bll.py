from dal.abstract_rates import RateABC
from dal.dal_factory import RatesFactory

class RatesBll:
    __rate_dao: RateABC

    def __init__(self, data_source: str):
        self.__rate_dao = RatesFactory().create_instance(data_source)

    def get_rates_data(self):
        return self.__rate_dao.get_rates()

    def convert_amount(self, source: str, target: str, amount: float):
    source = source.upper()
    target = target.upper()
    get_rate = self.__rate_dao.get_currency_rate

    try:
        source_rate = 1.0 if source == "PHP" else get_rate(source)
        target_rate = 1.0 if target == "PHP" else get_rate(target)

        php_amount = float(amount) * source_rate
        return php_amount / target_rate

    except Exception as ex:
        print(f"Value not in the list. {str(ex)}")

