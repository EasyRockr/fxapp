from controller.convert_controller import ConvertMoney
from controller.input_controller import InputController

class ConvertMenu:
    def __init__(self, data_source: str):
        self.data_source = data_source

    def input_menu(self):
        print("-------------------------------")
        input_ctrl = InputController(self.data_source)
        convert_ctrl = ConvertMoney(self.data_source)

        source = input_ctrl.get_currency("Source Ccy")
        if not source:
            return None

        target = input_ctrl.get_currency("Target Ccy")
        if not target:
            return None

        amount = input_ctrl.get_amount(f"Amount in {source}")
        if amount is None:
            return None

        result = convert_ctrl.convert(source, target, amount)
        if result is not None:
            formatted_result = f"{result:,.2f}"
            print(f"Converted Amt: {formatted_result} {target}")
