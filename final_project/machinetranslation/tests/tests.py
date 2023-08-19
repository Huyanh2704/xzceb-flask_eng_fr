from translator import englishtofrench, frenchtoenglish
import unittest

class TestE2F (unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishtofrench('School'), 'Lecole')

class TestF2E (unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchtoenglish('Fleur'), 'Flow')

unittest.main()