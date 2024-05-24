
from interactive_menu.src.interactive_menu import InteractiveMenu

class MainMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)
        self.sub_menu_modules = [
            AddMenu(manager, self.path),
            ShowMenu(manager, self.path),
            #MigrateMenu(manager, self.path)
        ]

    def title(self):
        return "Main"


class AddMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)

    def title(self):
        return "Add"

    def main_loop(self):
        form_results = self.interactive_form(
            [
                {
                    "question": "What is the name of the new location?",
                    "expected_response_type": "VARCHAR",
                    "return_as": "location_name",
                    "default": "",
                    "allow_empty": False
                },
                {
                    "question": "What is the x coord?",
                    "expected_response_type": "INT",
                    "return_as": "x_coord",
                    "default": "",
                    "allow_empty": False
                },
                {
                    "question": "What is the y coord?",
                    "expected_response_type": "INT",
                    "return_as": "y_coord",
                    "default": "",
                    "allow_empty": False
                },
                {
                    "question": "What is the z coord? REMEMBER TO INVERT THIS ONE",
                    "expected_response_type": "INT",
                    "return_as": "z_coord",
                    "default": "",
                    "allow_empty": False
                },
                {
                    "question": "What is the type of location?",
                    "expected_response_type": "VARCHAR",
                    "return_as": "location_type",
                    "default": "",
                    "allow_empty": False
                },
                {
                    "question": "What is the color of the new location?",
                    "expected_response_type": "VARCHAR",
                    "return_as": "location_color",
                    "default": "",
                    "allow_empty": False
                },
                {
                    "question": "What is the marker size of the new location?",
                    "expected_response_type": "INT",
                    "return_as": "location_size",
                    "default": "",
                    "allow_empty": False
                },
            ]
        )
        if form_results["user_accept"] != True:
            print("Aborting!")
            return
        form_results.pop("user_accept")
        for answer_key in form_results.keys():
            if not form_results[answer_key]["valid"]:
                print("%s is not a valid value! Aborting" % answer_key)
                return
        self.manager.add_location(
            form_results['location_name']['value'],
            int(form_results['x_coord']['value']),
            int(form_results['y_coord']['value']),
            int(form_results['z_coord']['value']),
            form_results['location_type']['value'],
            form_results['location_color']['value'],
            int(form_results['location_size']['value'])
        )


class ShowMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)

    def title(self):
        return "Show"

    def main_loop(self):
        self.manager.figure()


class MigrateMenu(InteractiveMenu):

    def __init__(self, manager, path=[]):
        super().__init__(manager, path)

    def title(self):
        return "Migrate"

    def main_loop(self):
        self.manager.migrate_data()

