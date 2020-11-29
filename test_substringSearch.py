import unittest
import random
import substring_search


class TestSubstringSearch(unittest.TestCase):
    "Unit tests for KMP_search."

    search = substring_search.Substring_search("haystacklist", "stack", 0, 0)

    # test case for brute force
    def test_BruteForce(self):
        res = self.search.brute_force("haystacklist", "stack", 0, 0)
        self.assertEqual(
            res, 3, "BruteForce({!r}, {!r})".format(
                "haystacklist", "stack"))

    # test case for KMP_search
    def test_KMP(self):
        res = self.search.kmpSearch("haystacklist", "stack")
        self.assertEqual(
            res, 3, "KMP_search({!r}, {!r})".format(
                "haystacklist", "stack"))

    # test case for Boyer Moore
    def test_boyer(self):
        boyerFound = self.search.search("haystacklist", "stack")
        self.assertEqual(
            boyerFound,
            3,
            "BoyerMoore_search({!r}, {!r})".format(
                "haystacklist",
                "stack"))

    # test case for Rabin Karp
    def test_RabinKarp(self):
        res = self.search.rabinKarp()
        self.assertEqual(
            res, 3, "rabinKarp({!r}, {!r})".format(
                "haystacklist", "stack"))

    # Test the algorithms with random texts and patterns
    def test_randomString(self):
        for k in range(1, 100):
            # Generate a random test case with k characters.
            haystack = ''.join(random.choices('abc', k=k))
            start, stop = sorted(random.sample(range(k + 1), 2))
            needle = haystack[start:stop]

            expected = []
            index = -1
            while True:
                index = haystack.find(needle, index + 1)
                if index == -1:
                    break
                expected.append(index)

            # KMP_search
            kmpFound = self.search.kmpSearch(haystack, needle)
            self.assertEqual(kmpFound, expected[0],
                             "KMP_search({!r}, {!r})".format(haystack, needle))

            # Boyer Moore
            boyerFound = self.search.search(haystack, needle)
            self.assertEqual(boyerFound, expected[0],
                             "BoyerMoore({!r}, {!r})".format(haystack, needle))


if __name__ == '__main__':
    unittest.main()
