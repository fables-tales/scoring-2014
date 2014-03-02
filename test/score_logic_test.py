
import os
import yaml

import helpers

from score_logic import score_team

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
