from datetime import datetime
from pathlib import Path

import pytest

from distinctdeer import editor, parser


def get_test_markdown(filename: str) -> str:
    test_file = Path(__file__).parent / "data" / filename
    return test_file.read_text()


def test_mark_as_checked():
    content = get_test_markdown("simple.md")

    # Test marking an unchecked item
    updated_content = editor.mark_as_checked(content, "test1")
    today = datetime.now().strftime("%Y-%m-%d")
    assert f"- [x] test1 ✅ {today}" in updated_content

    # Test item not found
    with pytest.raises(ValueError):
        editor.mark_as_checked(content, "nonexistent")

    # Test already checked item
    with pytest.raises(ValueError):
        editor.mark_as_checked(content, "test2")


def test_mark_as_checked_preserves_newline():
    content = get_test_markdown("simple.md")
    updated_content = editor.mark_as_checked(content, "test1")
    assert updated_content.endswith("\n"), "Updated content should end with newline"

    # Count the number of newlines at the end to ensure we're not adding extras
    assert not updated_content.endswith("\n\n"), (
        "Updated content should not have multiple trailing newlines"
    )


def test_mark_as_checked_integration(tmp_path):
    # Create a temporary markdown file
    test_file = tmp_path / "test.md"
    content = get_test_markdown("simple.md")
    test_file.write_text(content)

    # Mark item as checked
    updated_content = editor.mark_as_checked(test_file.read_text(), "test1")
    test_file.write_text(updated_content)

    # Verify the change
    parsed_data = parser.parse_markdown(test_file.read_text())
    assert "test1" in parsed_data.used["Test Section"]
    assert "test1" not in parsed_data.unused["Test Section"]

    # Verify file ends with exactly one newline
    file_content = test_file.read_text()
    assert file_content.endswith("\n"), "File should end with newline"
    assert not file_content.endswith("\n\n"), (
        "File should not have multiple trailing newlines"
    )


def test_workflow_find_and_mark_unused():
    # Start with test markdown
    content = get_test_markdown("test_markdown.md")
    parsed_data = parser.parse_markdown(content)

    # Find an unused name from the Colors section
    assert "bluebear" in parsed_data.unused["Colors"]
    assert "bluebear" not in parsed_data.used["Colors"]

    # Mark it as checked
    updated_content = editor.mark_as_checked(content, "bluebear")

    # Parse the updated content
    updated_data = parser.parse_markdown(updated_content)

    # Verify the change
    assert "bluebear" in updated_data.used["Colors"]
    assert "bluebear" not in updated_data.unused["Colors"]

    # Verify the date was added
    today = datetime.now().strftime("%Y-%m-%d")
    assert f"- [x] bluebear ✅ {today}" in updated_content
    assert updated_content.endswith("\n")
