import pytest
from string_utils import reverse_string, count_vowels


@pytest.fixture
def sample_text():
    return "hello world"


def test_reverse_string(sample_text):
    result = reverse_string(sample_text)
    assert result == "dlrow olleh"


def test_count_vowels(sample_text):
    result = count_vowels(sample_text)
    assert result == 3