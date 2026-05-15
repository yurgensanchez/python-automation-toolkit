from automation_toolkit.text_tools import clean_text


def test_clean_text_strips_and_collapses_spaces() -> None:
    assert clean_text("  Hello     from\nPython  ") == "Hello from Python"


def test_clean_text_can_lowercase() -> None:
    assert clean_text("  HELLO World  ", lowercase=True) == "hello world"
