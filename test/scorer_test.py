import sys
import os

from mock import Mock
path = os.path.dirname(os.path.realpath(__file__)) + "/../lib/"
sys.path.insert(0, path)
print sys.path

from scorer import Scorer
