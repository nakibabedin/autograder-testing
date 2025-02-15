import unittest
from config import EXCECUTION_DIR
from gradescope_utils.autograder_utils.decorators import weight, tags, visibility
import subprocess

class TestInventory(unittest.TestCase):
   def setUp(self):
      self.longMessage = False
      self.success = False

   def tearDown(self):
      if self.success: print("Your program passed the tests.")
      if not self.runOutput: pass
      self.runOutput.terminate()

   def runCase(self, queryFlags):
      # Get the raw output & remove whitespaces
      self.getOutput(queryFlags)
      formatted = self.raw.replace(' ', '').replace('\n', '').replace('\r', '').lower()

      did_pass = "success!" in formatted and '0failed' in formatted

      print(self.raw)

      self.assertTrue(expr=did_pass, msg=self.raw)
      self.success = True

   def getOutput(self, queryFlags):
      self.runOutput = subprocess.Popen(['./main', '-ni', '-d'] + queryFlags, 
                                        stdin=subprocess.PIPE, 
                                        stdout=subprocess.PIPE,  
                                        stderr=subprocess.PIPE,
                                        cwd=EXCECUTION_DIR)

      raw, err = self.runOutput.communicate()
      self.raw = raw.decode("utf8")
      self.err = err.decode("utf8")

   @weight(100)
   @tags("Test Description")
   def testDemos(self):
      """Test Description"""
      self.runCase(queryFlags=['--test-suite=Helloworld*', '--test-case=Helloworld*'])

if __name__ == "__main__":
    unittest.main()
