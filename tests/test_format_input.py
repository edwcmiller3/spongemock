from src.spongemock import format_input

def test_text_only():
    mock = "Supercalifragilisticexpialidocious"
    chars, non_chars = format_input(mock)
    assert len(chars) == len(mock) and len(non_chars) == 0