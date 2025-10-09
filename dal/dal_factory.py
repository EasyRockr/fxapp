from dal.rates_dal import RateDao
from dal.abstract_rates import RateABC
from util.logger import enable_logging


class RatesFactory:
    @enable_logging
    def create_instance(self, data_source: str) -> RateABC:
        obj_map = {
            "json": RateDao
        }
        dao_class = obj_map.get(data_source)
        if dao_class is None:
            raise Exception(f"[Error] Invalid data source.")
        return dao_class()
