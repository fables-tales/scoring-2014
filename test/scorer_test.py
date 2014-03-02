
import mock
import os
import yaml

import helpers

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

def test_isolated_scores():
    mock_tidy_zones = mock.Mock()
    mock_tidy_slots = mock.Mock()

    zones_1 = 'zones_1'
    zones_2 = 'zones_2'
    slots_1 = 'slots_1'
    slots_2 = 'slots_2'

    zones_1_out = 'zones_1_out'
    zones_2_out = 'zones_2_out'
    slots_1_out = 'slots_1_out'
    slots_2_out = 'slots_2_out'

    input_ = {
        "TLA1": {
            "robot_moved": False,
            "zone_tokens": zones_1,
            "slot_bottoms": slots_1,
            "upright_tokens": 0,
        },
        "TLA2": {
            "robot_moved": True,
            "zone_tokens": zones_2,
            "slot_bottoms": slots_2,
            "upright_tokens": 2,
        },
    }

    expected_zones = { "TLA1": zones_1, "TLA2": zones_2 }
    expected_slots = { "TLA1": slots_1, "TLA2": slots_2 }

    expected_zones_out = { "TLA1": zones_1_out, "TLA2": zones_2_out }
    expected_slots_out = { "TLA1": slots_1_out, "TLA2": slots_2_out }

    mock_tidy_zones.return_value = expected_zones_out
    mock_tidy_slots.return_value = expected_slots_out

    expected = {
        "TLA1": {
            "robot_moved": False,
            "zones_owned": zones_1_out,
            "slots_owned": slots_1_out,
            "upright_tokens": 0,
        },
        "TLA2": {
            "robot_moved": True,
            "zones_owned": zones_2_out,
            "slots_owned": slots_2_out,
            "upright_tokens": 2,
        },
    }

    with mock.patch('scorer.tidy_zones', mock_tidy_zones), \
            mock.patch('scorer.tidy_slots', mock_tidy_slots):

        scorer = Scorer(input_)
        actual = scorer.isolated_scores

        mock_tidy_zones.assert_called_once_with(expected_zones)
        mock_tidy_slots.assert_called_once_with(expected_slots)

        assert actual == expected, "Wrong isolated scores."
