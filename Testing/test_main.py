"""
To run "python -m unittest -v"
file and function name should start with test_ 
"""

import unittest
import script

class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        print("==== Will Run before test ====")
        
    def test_do_stuff(self):
        """do stuff"""
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)
 
    def test_do_stuff2(self):
        test_param = 'shsgffjjh'
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
 
    def test_do_stuff3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')
 
    def test_do_stuff4(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def tearDown(self) -> None:
        print("---Cleaning Up---")
        
if __name__ == '__main__':
    unittest.main()