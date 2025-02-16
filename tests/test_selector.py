import pytest

from distinctdeer import selector


def get_test_markdown(filename: str) -> str:
    from pathlib import Path

    test_file = Path(__file__).parent / "data" / filename
    return test_file.read_text()


def test_select_random_unused():
    content = get_test_markdown("test_markdown.md")

    # Test multiple selections to ensure randomness and validity
    for _ in range(10):
        selected = selector.select_random_unused(content)
        assert selected in ["sleepysloth", "dancingdolphin", "bluebear", "yellowyak"]


def test_select_random_unused_no_options():
    content = """# Test Section
- [x] test1 ✅ 2025-02-01
- [x] test2 ✅ 2025-02-01"""

    with pytest.raises(selector.NoUnusedNamesError) as excinfo:
        selector.select_random_unused(content)
    assert str(excinfo.value) == "No unused names available"


def test_select_random_unused_empty_file():
    content = ""

    with pytest.raises(selector.NoUnusedNamesError) as excinfo:
        selector.select_random_unused(content)
    assert str(excinfo.value) == "No unused names available"


def test_select_random_unused_no_names():
    content = """# Test Section
# Another Section
## Subsection"""

    with pytest.raises(selector.NoUnusedNamesError) as excinfo:
        selector.select_random_unused(content)
    assert str(excinfo.value) == "No unused names available"
