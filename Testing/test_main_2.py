import unittest
import script


class TestMain(unittest.TestCase):
    
    def test_do_stuff(self):
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result,15)

    def test_do_stuff2(self):
        test_param = 'Jawad'
        result = script.do_stuff(test_param)
        self.assertTrue(isinstance(result,ValueError))
    
    def test_value_error(self):
        test_param = 'Ahmad'
        result = script.do_stuff(test_param)
        self.assertIsInstance(result,ValueError)
    
    def test_null(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result,'Please enter a number')

    def test_empty(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result,'Please enter a number')

if __name__  == '__main__':      
    unittest.main()    
else:
    print("File imported, not running unit tests")