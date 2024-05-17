
from interactive_menu.src.interactive_menu import InteractiveMenu

class MainMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)
        self.sub_menu_modules = [
            AddMenu(manager, self.path),
            ShowMenu(manager, self.path),
        ]

    def title(self):
        return "Main"


class AddMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)

    def title(self):
        return "Add"

    def main_loop(self):
        print("Adding a place")


class ShowMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)

    def title(self):
        return "Show"

    def main_loop(self):
        self.manager.figure()

