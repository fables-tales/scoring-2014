
import os
import yaml

import helpers

from score_logic import score_team, tidy_slots, tidy_zones, validate_team

def test_score_team_zero():
    score_data = {
        "robot_moved": False,
        "zones_owned": [],
        "slots_owned": [],
        "upright_tokens": 0,
    }
    score = score_team(score_data)
    assert score == 0


def test_score_team_movement():
    score_data = {
        "robot_moved": True,
        "zones_owned": [],
        "slots_owned": [],
        "upright_tokens": 0,
    }
    score = score_team(score_data)
    assert score == 1


def test_score_team_upright_tokens_1():
    score_data = {
        "robot_moved": True,
        "zones_owned": [],
        "slots_owned": [],
        "upright_tokens": 1,
    }
    score = score_team(score_data)
    assert score == 2

def test_score_team_upright_tokens_2():
    score_data = {
        "robot_moved": True,
        "zones_owned": [],
        "slots_owned": [],
        "upright_tokens": 3,
    }
    score = score_team(score_data)
    assert score == 4


def test_score_team_zones_1():
    score_data = {
        "robot_moved": True,
        "zones_owned": [0],
        "slots_owned": [],
        "upright_tokens": 0,
    }
    score = score_team(score_data)
    assert score == 2

def test_score_team_zones_2():
    score_data = {
        "robot_moved": True,
        "zones_owned": [0, 1],
        "slots_owned": [],
        "upright_tokens": 0,
    }
    score = score_team(score_data)
    assert score == 3


def test_score_team_slots_1():
    score_data = {
        "robot_moved": True,
        "zones_owned": [],
        "slots_owned": [0],
        "upright_tokens": 0,
    }
    score = score_team(score_data)
    assert score == 2

def test_score_team_slots_separate():
    score_data = {
        "robot_moved": True,
        "zones_owned": [],
        "slots_owned": [0, 2],
        "upright_tokens": 0,
    }
    score = score_team(score_data)
    assert score == 3

def test_score_team_slots_adjacent():
    score_data = {
        "robot_moved": True,
        "zones_owned": [],
        "slots_owned": [0, 1],
        "upright_tokens": 0,
    }
    score = score_team(score_data)
    assert score == 5

def test_score_team_slots_some_adjacent():
    score_data = {
        "robot_moved": True,
        "zones_owned": [],
        "slots_owned": [0, 1, 3],
        "upright_tokens": 0,
    }
    score = score_team(score_data)
    assert score == 6

def test_score_team_slots_two_adjacent_pairs():
    score_data = {
        "robot_moved": True,
        "zones_owned": [],
        "slots_owned": [0, 1, 4, 5],
        "upright_tokens": 0,
    }
    score = score_team(score_data)
    assert score == 9

def test_score_team_slots_around_end():
    # Slots 3 and 4 are numerically adjacent, but don't qualify for the bonus
    score_data = {
        "robot_moved": True,
        "zones_owned": [],
        "slots_owned": [3, 4],
        "upright_tokens": 0,
    }
    score = score_team(score_data)
    assert score == 3


def test_score_team_mixed_1():
    score_data = {
        "robot_moved": True,
        "zones_owned": [1, 2],
        "slots_owned": [0, 1, 3],
        "upright_tokens": 4,
    }
    score = score_team(score_data)
    assert score == 12


def test_tidy_slots_empty():
    input_ = {
        'TLA1' : { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0 },
        'TLA2' : { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0 },
    }

    expected = {
        'TLA1' : set(),
        'TLA2' : set(),
    }

    actual = tidy_slots(input_)

    assert actual == expected

def test_tidy_slots_simple():
    input_ = {
        'TLA1' : { 0: 1, 1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0 },
        'TLA2' : { 0: 0, 1: 0, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0 },
    }

    expected = {
        'TLA1' : set([0, 1]),
        'TLA2' : set([2, 3]),
    }

    actual = tidy_slots(input_)

    assert actual == expected

def test_tidy_slots_clash():
    input_ = {
        'TLA1' : { 0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0 },
        'TLA2' : { 0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0 },
    }

    threw = False
    try:
        tidy_slots(input_)
    except Exception as e:
        threw = True

    assert threw, "Should have complained about invalid input."


def test_tidy_zones_empty():
    input_ = {
        'TLA1' : { 0: 0, 1: 0, 2: 0, 3: 0 },
        'TLA2' : { 0: 0, 1: 0, 2: 0, 3: 0 },
    }

    expected = {
        'TLA1' : set(),
        'TLA2' : set(),
    }

    actual = tidy_zones(input_)

    assert actual == expected

def test_tidy_zones_simple():
    input_ = {
        'TLA1' : { 0: 1, 1: 1, 2: 0, 3: 0 },
        'TLA2' : { 0: 0, 1: 0, 2: 1, 3: 1 },
    }

    expected = {
        'TLA1' : set([0, 1]),
        'TLA2' : set([2, 3]),
    }

    actual = tidy_zones(input_)
    assert actual == expected

def test_tidy_zones_overlap():
    input_ = {
        'TLA1' : { 0: 1, 1: 0, 2: 0, 3: 0 },
        'TLA2' : { 0: 2, 1: 0, 2: 0, 3: 0 },
    }

    expected = {
        'TLA1' : set(),
        'TLA2' : set([0]),
    }

    actual = tidy_zones(input_)
    assert actual == expected

def test_tidy_zones_tie():
    input_ = {
        'TLA1' : { 0: 1, 1: 0, 2: 0, 3: 0 },
        'TLA2' : { 0: 1, 1: 0, 2: 0, 3: 0 },
    }

    expected = {
        'TLA1' : set(),
        'TLA2' : set(),
    }

    actual = tidy_zones(input_)
    assert actual == expected

def test_tidy_zones_mixed():
    input_ = {
        'TLA1' : { 0: 1, 1: 4, 2: 0, 3: 0 },
        'TLA2' : { 0: 1, 1: 1, 2: 2, 3: 0 },
    }

    expected = {
        'TLA1' : set([1]),
        'TLA2' : set([2]),
    }

    actual = tidy_zones(input_)
    assert actual == expected


def assert_threw(action, message):
    threw = False
    try:
        action()
    except Exception as e:
        threw = True
        return e
    finally:
        assert threw, message

def plain_input():
    return {
        "zone": 0,
        "robot_moved": False,
        "zone_tokens": {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
        },
        "slot_bottoms": {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
        },
        "upright_tokens": 0
    }

def test_validate_team():
    input_ = plain_input()
    validate_team('TLA2', input_)

def test_validate_team_missing_item():
    def assert_invalid(remove):
        input_ = plain_input()
        del input_[remove]
        assert remove not in input_, "Wut"
        e = assert_threw(lambda: validate_team('TLA9', input_), \
                         "Should error when missing key '{}'.".format(remove))

        assert remove in e.message

    for k in ["robot_moved", "zone_tokens", \
              "slot_bottoms", "upright_tokens"]:
        yield assert_invalid, k

def assert_invalid(input_, expected_msg_part, error_message):
    tla = 'TLA9'
    e = assert_threw(lambda: validate_team(tla, input_), error_message)
    assert expected_msg_part in e.message
    assert tla in e.message

def test_validate_team_missing_some_slots():
    input_ = plain_input()

    input_['slot_bottoms'] = dict(zip(range(7), [0]*7))

    assert_invalid(input_, 'missing information for slot', "Should error when missing slots")

def test_validate_team_missing_some_zones():
    input_ = plain_input()

    input_['zone_tokens'] = dict(zip(range(3), [0]*3))

    assert_invalid(input_, 'missing information for zone', "Should error when missing zones")

def test_validate_team_zones_negative_count():
    input_ = plain_input()

    input_['zone_tokens'][0] = -1

    assert_invalid(input_, 'negative', "Should error when a zone has a negative token count")

def test_validate_team_too_many_tokens_in_zones():
    input_ = plain_input()

    # 12 overall
    rng = range(4)
    input_['zone_tokens'] = dict(zip(rng, [3]*4))

    assert_invalid(input_, 'too many tokens', "Should error when too many tokens")

def test_validate_team_too_many_tokens_overall():
    input_ = plain_input()

    # 9 overall, since slots aren't in zones
    input_['zone_tokens'][0] = 1
    input_['slot_bottoms'] = dict(zip(range(8), [1]*8))

    assert_invalid(input_, 'too many tokens', "Should error when too many tokens")
