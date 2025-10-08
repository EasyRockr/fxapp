from controller.rates_controller import RatesController

class PageRates:
    def __init__(self, data_source: str):
        self.rate_controller = RatesController(data_source)

    def display_rates(self):
        print("\n-------------- Fx Rates --------------")
        print("Source Ccy \t Target Ccy \t Rate")
        print("---------------------------------------")
        
        rates_data = self.rate_controller.retrieve_rates()
        for currency, rate in rates_data["rates"].items():
            print(f"{currency}\t\tPHP\t\t{rate:.4f}")
        
        print("---------------------------------------")
        print(f"Base Ccy: {rates_data['base']}")
        print(f"Date: {rates_data['date']}\n")
