import unittest
from truncate import truncate

class Teststringcode(unittest.TestCase): 
    def test_ok(self):
        self.assertEqual(truncate('heqingyang',5) , 'heqin...' )
        self.assertEqual(truncate('heqingyang',20) , 'heqingyang' )

if __name__ == '__main__':
    unittest.main()
