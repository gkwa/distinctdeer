from pathlib import Path

from distinctdeer import parser


def get_test_markdown(filename: str) -> str:
    test_file = Path(__file__).parent / "data" / filename
    return test_file.read_text()


def test_parse_markdown():
    content = get_test_markdown("test_markdown.md")
    data = parser.parse_markdown(content)

    # Test used items
    assert "Animals" in data.used
    assert "happyhedgehog" in data.used["Animals"]
    assert "jumpingjellyfish" in data.used["Animals"]
    assert len(data.used["Animals"]) == 2

    assert "Colors" in data.used
    assert "redrabbit" in data.used["Colors"]
    assert "greengorilla" in data.used["Colors"]
    assert len(data.used["Colors"]) == 2

    # Test unused items
    assert "Animals" in data.unused
    assert "sleepysloth" in data.unused["Animals"]
    assert "dancingdolphin" in data.unused["Animals"]
    assert len(data.unused["Animals"]) == 2

    assert "Colors" in data.unused
    assert "bluebear" in data.unused["Colors"]
    assert "yellowyak" in data.unused["Colors"]
    assert len(data.unused["Colors"]) == 2
