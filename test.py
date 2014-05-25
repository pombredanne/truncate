import unittest
import truncate

class TestTruncate(unittest.TestCase): 

	def testLimit(self):
		self.assertEqual(truncate('heqingyang', 5) , 'heqin...')
		self.assertEqual(truncate('heqingyang', 20) , 'heqingyang')

	def testEllipsis(self):
		self.assertEqual(truncate('heqingyang', 5) , 'heqin...')
		self.assertEqual(truncate('heqingyang', 5, ellipsis=' more') , 'heqin more')


if __name__ == '__main__':
    unittest.main()
