from src.spongemock import mock_text

def test_empty_string():
    assert mock_text('') == ''

def test_mock_string():
    mock = "ThIs Is AlReAdY mOcKeD"
    assert mock_text(mock) == mock