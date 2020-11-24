import unittest
import random
import substring_search


class TestSubstringSearch(unittest.TestCase):
    "Unit tests for KMP_search."

    def test_KMP(self):
        res = substring_search.KMP_search("haystacklist", "stack")
        self.assertEqual(res, 3,
                         "KMP_search({!r}, {!r})".format("haystacklist", "stack"))

    def test_boyer(self):
        boyerFound = substring_search.search("haystacklist", "stack")
        self.assertEqual(boyerFound, 3,
                         "BuyerMoore_search({!r}, {!r})".format("haystacklist", "stack"))

    def test_randomString(self):
        for k in range(1, 100):
            # Generate a random test case with k characters.
            haystack = ''.join(random.choices('abc', k=k))
            start, stop = sorted(random.sample(range(k + 1), 2))
            needle = haystack[start:stop]

            # Use Python's built-in str.find to compute the expected result.
            expected = []
            index = -1
            while True:
                index = haystack.find(needle, index + 1)
                if index == -1:
                    break
                expected.append(index)

            # Compare with the actual result.
            found = substring_search.KMP_search(haystack, needle)
            self.assertEqual(found, expected[0],
                             "KMP_search({!r}, {!r})".format(haystack, needle))

            boyerFound = substring_search.search(haystack, needle)
            self.assertEqual(boyerFound, expected[0],
                             "BuyerMoore_search({!r}, {!r})".format(haystack,
                                                                    needle))


if __name__ == '__main__':
    unittest.main()
