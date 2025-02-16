import random

from . import parser


class NoUnusedNamesError(Exception):
    pass


def select_random_unused(content: str) -> str:
    """Select a random unused project name from the markdown content."""
    data = parser.parse_markdown(content)

    # Collect all unused names
    all_unused = []
    for section, names in data.unused.items():
        all_unused.extend(names)

    if not all_unused:
        raise NoUnusedNamesError("No unused names available")

    return random.choice(all_unused)
