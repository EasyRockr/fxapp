from controller.convert_controller import ConvertMoney
from controller.input_controller import InputController

class ConvertMenu:
    def __init__(self, data_source: str):
        self.data_source = data_source

    def input_menu(self):
        print("-------------------------------")
        input_ctrl = InputController(self.data_source)
        convert_ctrl = ConvertMoney(self.data_source)

        source = target = amount = None

        while True:
            try:
                if source is None:
                    source = input_ctrl.get_currency("Source Ccy")
                if target is None:
                    target = input_ctrl.get_currency("Target Ccy")
                if amount is None:
                    amount = input_ctrl.get_amount(f"Amount in {source}")
                break
            except ValueError as e:
                print(e)
                if "currency" in str(e).lower() and source is None:
                    continue
                elif "currency" in str(e).lower() and target is None:
                    continue
                elif "amount" in str(e).lower():
                    amount = None
                else:
                    source = target = amount = None

        try:
            result = convert_ctrl.convert(source, target, amount)
            print(f"Converted amount: {result:,.2f} {target}")
        except Exception as e:
            print(f"[Error] Conversion failed. [Info] {str(e)}")