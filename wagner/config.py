import argparse


def parse_args() -> dict:
    parser = argparse.ArgumentParser(description="Wagner help")
    parser.add_argument(
        "-v",
        "--version",
        help="The version of the wagner application.",
        dest="version",
        action="store_true",
    )

    args = parser.parse_args()

    return args


prog = "wagner"
version = "0.1"
