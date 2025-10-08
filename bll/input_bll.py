from dal.dal_factory import RatesFactory

class InputBll:
    def __init__(self, data_source: str):
        self.rate_dao = RatesFactory().create_instance(data_source)
        data = self.rate_dao.get_rates()
        self.valid_currencies = list(data["rates"].keys())

    def get_menu_choice(self, valid_choices: list[int]):
        val = input("Option: ").strip()
        if not val.isdigit():
            raise ValueError("[Error] Invalid input. Enter a number.")
        choice = int(val)
        if choice not in valid_choices:
            raise ValueError(f"[Warn] Invalid option. Choose from {valid_choices}.")
        return choice

    def get_currency(self, label: str):
        val = input(f"{label}: ").strip().upper()
        if val not in self.valid_currencies:
            raise ValueError(f"[Error] Invalid currency '{val}'. [Info] Valid: {', '.join(self.valid_currencies)}.")
        return val

    def get_amount(self, label: str):
        val = input(f"{label}: ").strip()
        try:
            num = float(val)
        except ValueError:
            raise ValueError("[Error] Invalid amount. Enter a valid number.")
        if val.startswith("-0"):
            raise ValueError("[Error] Negative zero (-0) is not allowed.")
        if num < 0:
            raise ValueError("[Error] Amount cannot be negative.")
        return round(num, 2)



# dal = walang business layer, purely data access (purely data persistence)
# bll = all business logic
# data validator = not tighly couple to input validator
# input -> data validator
# the same validator can be placed in the bll
# you can validate anything = regex (date, money, string), easiest way (no need for allow validators)
# 2 inputs: pattern, value -> validate
# iso date validation pattern
# + integer pattern, small case string pattern
# can create/specify the regex