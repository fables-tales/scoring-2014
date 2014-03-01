#!/usr/bin/env python

import os
import sys
import yaml

path = os.path.dirname(os.path.realpath(__file__)) + "/lib/"
sys.path.insert(0, path)
from score_parser import ScoreParser
from scorer import Scorer

def main(file_reader):
    parsed_match = ScoreParser(yaml.load).parse(file_reader.read())
    scorer = Scorer()
    scores = scorer.produce_scores(parsed_match)
    return {
        "version"      : "1.0.0",
        "match_number" : parsed_match["match_number"],
        "scores"       : scores,
    }

if __name__ == "__main__":

    # Proton says read from stdin if no file.
    reader = sys.stdin

    if len(sys.argv) > 1:
        # But let's be helpful if we can
        if sys.argv[1] in ['-h', '--help']:
            exit("Usage: {} SCORES_YAML".format(sys.argv[0]))
        else:
            reader = open(sys.argv[1], 'r')

    output = main(reader)
    print yaml.dump(output)
