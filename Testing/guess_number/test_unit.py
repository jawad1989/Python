import unittest
import script

class TestMain(unittest.TestCase):
    def test_input(self):
        result = script.guess_number(5,5)
        print(f'result = {result}')
        self.assertTrue(result)

unittest.main()
