# SRobo 2014 Scorer

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

Run tests with `nosetests` from the root.
