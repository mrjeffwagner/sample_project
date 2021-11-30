from wagner import config

# import config


def handle_subcommands():
    args = config.parse_args()

    if args.version:
        exit(print(f"Version: {config.version}"))


def main():
    handle_subcommands()
    print("Wagner command is working!!!")


if __name__ == "__main__":
    exit(main())
