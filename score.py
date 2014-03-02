#!/usr/bin/env python

import os
import sys

path = os.path.dirname(os.path.realpath(__file__)) + "/lib/"
sys.path.insert(0, path)

from scorer import Scorer

path = os.path.join(path, "libproton/")
sys.path.insert(0, path)

import libproton

def score(teams_data):
    return Scorer().produce_scores(teams_data)

libproton.main(score)
