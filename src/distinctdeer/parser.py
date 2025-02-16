from typing import Dict, List, NamedTuple

from markdown_it import MarkdownIt


class ParsedData(NamedTuple):
    used: Dict[str, List[str]]
    unused: Dict[str, List[str]]


def parse_markdown(content: str) -> ParsedData:
    md = MarkdownIt()
    tokens = md.parse(content)

    current_section = ""
    used_items = {}
    unused_items = {}

    for token in tokens:
        if token.type == "heading_open":
            current_section = tokens[tokens.index(token) + 1].content
            used_items[current_section] = []
            unused_items[current_section] = []
        elif token.type == "list_item_open":
            item_tokens = tokens[tokens.index(token) + 1 : tokens.index(token) + 4]
            for item in item_tokens:
                if "[" in item.content and "]" in item.content:
                    project_name = item.content.split("]")[1].split("✅")[0].strip()
                    if current_section:
                        if item.content.startswith("[x]"):
                            used_items[current_section].append(project_name)
                        else:
                            unused_items[current_section].append(project_name)

    return ParsedData(used_items, unused_items)
