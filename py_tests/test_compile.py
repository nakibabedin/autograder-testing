import unittest
import os
from config import EXCECUTION_DIR
from gradescope_utils.autograder_utils.decorators import weight, tags


class TestOutput(unittest.TestCase):
    def setUp(self):
        pass

    @weight(5)
    @tags("compiles")
    def test_output(self):
        """ Test compiles """
        compiles = False
        list_of_files = os.listdir(EXCECUTION_DIR)
        for token in list_of_files:
            if 'main' in token and 'main.cpp' not in token and 'main.o' not in token:
                compiles = True
        if compiles:
            print("Your program compiles!")
            self.assertEqual(True, True)
        else:
            print("\nYour program does not compile. Please refer to the Project Specification. \n")
            self.assertEqual('Does not compile', '')

if __name__ == "__main__":
    unittest.main()
