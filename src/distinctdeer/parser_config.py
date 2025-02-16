import argparse
from pathlib import Path


def get_args() -> argparse.Namespace:
    main_parser = argparse.ArgumentParser(description="Parse markdown project names")
    main_parser.add_argument(
        "--path",
        type=Path,
        default="/Users/mtm/Documents/Obsidian Vault/project name examples.md",
        help="Path to markdown file",
    )

    subparsers = main_parser.add_subparsers(dest="command", help="Available commands")

    # Get command group
    get_parser = subparsers.add_parser("get", help="Retrieve project name information")
    get_subparsers = get_parser.add_subparsers(dest="subcommand", help="Get operations")

    # Get subcommands
    get_subparsers.add_parser("used", help="Show used (checked) project names")
    get_subparsers.add_parser("unused", help="Show unused (unchecked) project names")
    get_subparsers.add_parser("all", help="Show all project names")
    get_subparsers.add_parser(
        "rand", help="Get a random unused project name without marking it"
    )

    # Use command group
    use_parser = subparsers.add_parser("use", help="Use or mark project names")
    use_subparsers = use_parser.add_subparsers(dest="subcommand", help="Use operations")

    # Use subcommands
    check_parser = use_subparsers.add_parser(
        "check", help="Mark a project name as checked"
    )
    check_parser.add_argument("name", help="Project name to mark as checked")

    use_subparsers.add_parser(
        "rand", help="Select and mark a random unused project name"
    )

    return main_parser.parse_args()
