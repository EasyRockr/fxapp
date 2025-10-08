from abc import ABC

class RateABC(ABC):
    def get_rates(self) -> dict:
        pass

    def get_currency_rate(self, currency: str) -> float:
        pass
