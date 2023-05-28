#! /usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
	def test_baseic(self):
		testcase = "Mohammed, Iris"
		expected = "Iris Mohammed"
		self.assertEqual(rearrange_name(testcase), expected)

unittest.main()

