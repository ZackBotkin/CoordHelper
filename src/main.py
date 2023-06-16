import argparse
from src.coord_helper import CoordHelper

def main():
    print("Welcome to minecraft coordinate buddy")

    coord_helper = CoordHelper()
    #coord_helper.read_coords()
    coord_helper.figure()


if __name__ == "__main__":
    main()
