from pages.page_rates import PageRates
from pages.page_convert import ConvertMenu
from pages.page_main_menu import MainMenu

class Router:
    def __init__(self, data_source: str):
        self.data_source = data_source

    def route_choice(self):
        main_menu = MainMenu()
        pages = {
            1: PageRates(self.data_source).display_rates,
            2: ConvertMenu(self.data_source).input_menu
        }

        valid_choices = list(pages.keys())

        while True:
            try:
                choice = int(main_menu.display())
                if choice in valid_choices:
                    try:
                        pages[choice]()
                    except ValueError as e:
                        print(e)
                    except Exception as e:
                        print(f"[Error] {e}")
                else:
                    print(f"[Error] Invalid option. [Info] Please choose from {valid_choices}.")
            except ValueError:
                print(f"[Error] Invalid input. [Info] Please enter a number from {valid_choices}.")