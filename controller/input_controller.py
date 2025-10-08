from dal.input_dal import InputDal

class InputController:
    def __init__(self, data_source: str):
        self.input_dal = InputDal(data_source)

    def get_menu_choice(self, valid_choices: list[int]):
        return self.input_dal.get_menu_choice(valid_choices)

    def get_currency(self, label: str):
        return self.input_dal.get_currency(label)

    def get_amount(self, label: str):
        return self.input_dal.get_amount(label)
