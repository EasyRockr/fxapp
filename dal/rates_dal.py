from util.file_util import read_json_as_dict
from dal.abstract_rates import RateABC
from util.logger import enable_logging

class RateDao(RateABC):
    def __init__(self):
        self.fetched_currency = read_json_as_dict("rates.json")

    @enable_logging
    def get_rates(self) -> dict:
        return self.fetched_currency

    @enable_logging
    def get_currency_rate(self, currency: str) -> float:
        rates = self.fetched_currency["rates"]
        currency = currency.strip().upper()
        if currency not in rates:
            raise ValueError(f"[Error] Invalid currency: {currency}")
        return float(rates[currency])
