import unittest
import random


def anonymize_string(data):
    """Anonymizes a string by replacing each character with an asterisk."""
    return '*' * len(data)


def anonymize_list(data):
    """Anonymizes a list by shuffling the elements and returning the shuffled list."""
    shuffled_data = data.copy()
    random.shuffle(shuffled_data)
    return shuffled_data


def anonymize_unstructured_text(text):
    """Anonymizes unstructured text by replacing consecutive words with 'REDACTED'"""
    words = text.split()
    anonymized_words = []
    for word in words:
        if word.isalpha():
            anonymized_words.append('REDACTED')
        else:
            anonymized_words.append(word)
    return ' '.join(anonymized_words)


class TestAnonymization(unittest.TestCase):

    def test_anonymize_string(self):
        original_data = "Hello, World!"
        anonymized_data = anonymize_string(original_data)
        self.assertEqual(len(original_data), len(anonymized_data))
        self.assertEqual(anonymized_data, '*' * len(original_data))

    def test_anonymize_list(self):
        original_data = [1, 2, 3, 4, 5]
        anonymized_data = anonymize_list(original_data)
        self.assertEqual(len(original_data), len(anonymized_data))
        self.assertNotEqual(original_data, anonymized_data)
        self.assertEqual(sorted(original_data), sorted(anonymized_data))

    def test_anonymize_unstructured_text(self):
        original_data = "Hello World, this is a test. Let's see how it works!"
        anonymized_data = anonymize_unstructured_text(original_data)
        self.assertIn("REDACTED", anonymized_data)
        self.assertNotEqual(original_data, anonymized_data)
        self.assertEqual(len(original_data.split()), len(anonymized_data.split()))


if __name__ == '__main__':
    unittest.main()
