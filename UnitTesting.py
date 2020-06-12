import unittest



########################################

class TestStringMethods(unittest.testCase):

	def test_upper(self):
		self.assertEqual('foo'.upper(), 'FOO')


	def test_isupper(self):
			self.assertTrue('FOO'.isupper())
			self.assertFalse('FOO'.isupper())

	def test_split(self):

		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])

		#check that s.split fails when the seperator is not a string

		with self.assertiRaises(TypeError):
			s.split(2)

if __name__ == 'main'__':
	unittest.main()
