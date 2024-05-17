import argparse
from helper.src.config.config import Configs
from helper.src.context_manager import ContextManager
from helper.src.interactive.main_menu import MainMenu

def main():

    parser = argparse.ArgumentParser(description= 'default parser')
    parser.add_argument('--config_file', help='the configuration file')
    args = parser.parse_args()

    configs = Configs(args.config_file)
    context_manager = ContextManager(configs)
    menu = MainMenu(context_manager)
    menu.main_loop()

if __name__ == "__main__":
    main()
