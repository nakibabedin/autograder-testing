import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
import os

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('./')
    JSONTestRunner().run(suite)
