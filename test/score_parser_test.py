import sys
import os

from mock import Mock
path = os.path.dirname(os.path.realpath(__file__)) + "/../lib/"
sys.path.insert(0, path)
print sys.path
from score_parser import ScoreParser

def test_parser_invokes_given_loader_with_input():
    loader = Mock()
    value_to_be_parsed = Mock()

    p = ScoreParser(loader)
    p.parse(value_to_be_parsed)

    loader.assert_called_with(value_to_be_parsed)

def test_parser_returns_parsed_value_with_input():
    parsed_value = Mock()
    loader = Mock(return_value = parsed_value)
    value_to_be_parsed = Mock()

    p = ScoreParser(loader)
    assert p.parse(value_to_be_parsed) == parsed_value
