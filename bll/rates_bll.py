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
            source_rate = get_rate(source)
            target_rate = get_rate(target)

            base_amount = float(amount) * source_rate
            return round(base_amount / target_rate, 2)

        except KeyError:
            print(f"[Error] Invalid currency. Please check your rates list.")
