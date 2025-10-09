from dal.abstract_rates import RateABC
from dal.dal_factory import RatesFactory
from util.logger import enable_logging

class RatesBll:
    __rate_dao: RateABC

    def __init__(self, data_source: str):
        self.__rate_dao = RatesFactory().create_instance(data_source)

    @enable_logging
    def get_rates_data(self):
        return self.__rate_dao.get_rates()

    @enable_logging
    def convert_amount(self, source: str, target: str, amount: float):
        source = source.upper()
        target = target.upper()
        get_rate = self.__rate_dao.get_currency_rate

        if str(amount).startswith("-0") or amount < 0:
            raise ValueError("[Error] clark must not be negative.")
        if amount == 0:
            return 0.00

        try:
            source_rate = get_rate(source)
            target_rate = get_rate(target)
            base_amount = float(amount) * source_rate
            return round(base_amount / target_rate, 2)
        except ValueError as e:
            raise
        except ZeroDivisionError:
            raise ValueError("[Error] Target currency rate is zero. [Warn] Conversion aborted.")
        except Exception as e:
            raise ValueError(f"[Error] Conversion failed. [Info] {str(e)}")
