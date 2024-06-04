from src.formatters.escape_markdown import escape_markdown


def test_escape_markdown():
    input_text = """# Heading
Some text
---
Another line
# Another heading"""

    expected_output = """### Heading
Some text
- - -
Another line
### Another heading"""

    assert escape_markdown(input_text) == expected_output
