#!/usr/bin/env python

import os
import sys
import yaml

path = os.path.dirname(os.path.realpath(__file__)) + "/lib/"
sys.path.insert(0, path)
from score_parser import ScoreParser
from scorer import Scorer

def main(file_name):
    parsed_match = ScoreParser(yaml.load).parse(open(file_name).read())
    scorer = Scorer()
    scores = scorer.produce_scores(parsed_match)
    return {
        "version"      : "1.0.0",
        "match_number" : parsed_match["match_number"],
        "scores"       : scores,
    }

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Usage: {} SCORES_YAML".format(sys.argv[0]))
    main(sys.argv[1])
    print yaml.dump(
            {
                "version":"1.0.0",
            }
    )
