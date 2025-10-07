from dal.dal_factory import RatesFactory

class InputBll:
    def __init__(self, data_source: str):
        self.rate_dao = RatesFactory().create_instance(data_source)
        self.valid_currencies = list(self.rate_dao.get_rates()["rates"].keys()) + ["PHP"]
        print(self.valid_currencies) 

    def get_menu_choice(self, valid_choices: list[int]):
        while True:
            val = input("Option: ").strip()
            if not val.isdigit():
                print("[Error] Invalid input. Enter a number.")
                continue
            choice = int(val)
            if choice not in valid_choices:
                print(f"[Warn] Invalid option. Choose from {valid_choices}.")
                continue
            return choice

    def get_currency(self, label: str):
        while True:
            val = input(f"{label}: ").strip().upper()
            if val not in self.valid_currencies:
                print(f"[Error] Invalid currency '{val}'. [Info] Valid: {', '.join(self.valid_currencies)}.")
                continue
            return val

    def get_amount(self, label: str):
        while True:
            val = input(f"{label}: ").strip()
            try:
                num = float(val)
            except ValueError:
                print("[Error] Invalid amount. Enter a valid number.")
                continue

            if val.startswith("-0"):
                print("[Error] Negative zero (-0) is not allowed.")
                continue
            if num < 0:
                print("[Error] Amount cannot be negative.")
                continue

            return round(num, 2)
