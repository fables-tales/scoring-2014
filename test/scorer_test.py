
import os
import sys
import yaml

import helpers

path = os.path.dirname(os.path.realpath(__file__)) + "/../lib/"
sys.path.insert(0, path)
print sys.path

from scorer import Scorer

def check_by_input_file(input_name):
    input_file = os.path.join("test/data/scorer", input_name)

    test_data = yaml.load(open(input_file).read())
    scorer = Scorer(test_data['input'])
    scores = scorer.calculate_scores()

    expected_scores = test_data['scores']

    assert scores == expected_scores, "Incorrect scores for '{0}'.".format(input_name)

def test_input_file():
    inputs = helpers.get_input_files("test/data/scorer")

    for input_name in inputs:
        yield check_by_input_file, input_name
