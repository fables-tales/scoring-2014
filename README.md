# SRobo 2014 Scorer

[![Build Status](https://travis-ci.org/PeterJCLaw/scoring-2014.png)](https://travis-ci.org/PeterJCLaw/scoring-2014)

This is a script to calculate game scores for the [Student Robotics](https://www.studentrobotics.org)
2014 game entitled 'Slots'.
It complies with the [Proton](https://github.com/samphippen/proton)
specification for such scoring scripts.

To use it, copy and edit `templates/yaml_template.yaml`,
 and pass the name as the only command line argument.

Example:
~~~~
./score.py matches/001.yaml
~~~~

The input yaml file should look something like this
 (but you should _always_ use the template as detailed above!):
~~~~ .yaml
match_number: 0
teams:
  TLA1:
    zone: 0 # integer
    robot_moved: false # boolean
    zone_tokens:
      0: 0 # integer
      1: 0
      2: 0
      3: 0
    slot_bottoms:
      0: 0 # bool-ish value, suggested as 1 or 0
      # 1...6
      7: 0
    upright_tokens: 0 # integer
  TLA2:
    # etc.
~~~~

Run tests with `nosetests test` from the root.
