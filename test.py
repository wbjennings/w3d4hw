import unittest

from cart import Cart

class Test_Cart(unittest.TestCase):

    def test_no_args(self):
        result = Cart({'apple': {'quantity': 1, 'price': 1.2}})
        expected_output = {}
        self.assertEqual(result, expected_output)

    def test_string(self):
        result = Cart('Im a string!')
        expected_output = {'apple': {'quantity': 1, 'price': 1.2}}
        
if __name__ == '__main__':
    unittest.main()