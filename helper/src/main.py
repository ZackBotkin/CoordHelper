import argparse
from helper.src.context_manager import ContextManager
from helper.src.interactive.main_menu import MainMenu

def main():
    context_manager = ContextManager({"line_start": ">>>"})
    menu = MainMenu(context_manager)
    menu.main_loop()

if __name__ == "__main__":
    main()
