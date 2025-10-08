from util.file_util import read_json_as_dict
from dal.abstract_rates import RateABC

class RateDao(RateABC):
    def __init__(self):
        self.fetched_currency = read_json_as_dict("rates.json")

    def get_rates(self) -> dict:
        return self.fetched_currency

    def get_currency_rate(self, currency: str) -> float:
        rates = self.fetched_currency["rates"]
        rate = rates.get(currency)
        if rate is None:
            raise Exception(f"[Error] Invalid currency: {currency}")
        return float(rate)