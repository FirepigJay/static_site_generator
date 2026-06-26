import unittest
from main import extract_title

class TestExtractHeading(unittest.TestCase):
    def testExtractTitle(self):
        md = '# Hello'
        result = 'Hello'
        self.assertEqual(extract_title(md), result)