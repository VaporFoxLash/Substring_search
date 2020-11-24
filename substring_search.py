
class BruteForce(object):
    """docstring forBruteForce."""

    def __init__(self, haystack, needle, start_indx, found_indx):
        self.haystack = haystack
        self.needle = needle
        self.start_indx = start_indx
        self.found_indx = found_indx

    def brute_force(self, needle, haystack, start_indx = 0, found_indx = 0):
        if len(haystack) == 0:
            return found_indx

        if len(needle) == 0:
            return -1

        for i in iter(needle):
            start_indx += 1
            for j in iter(haystack):
                if i == j:
                    found_indx += start_indx - 1
                    return self.brute_force(needle[start_indx:],
                    haystack[1:], 0, found_indx)
                else:
                    break
        return -1


class KMP_search:
    """doc

     forKMP_search."""

    def __init__(self, haystack, needle):
        # superKMP_search, self).__init__()
        self.haystack = haystack
        self.needle = needle

    def get_prefix_table(self, needle):
        '''
        Creatae a prefix table to search in the string
        '''
        prefix_set = set()
        n = len(needle)
        prefix_table = [0] * n
        delimeter = 1
        while(delimeter < n):
            prefix_set.add(needle[:delimeter])
            j = 1
            while(j < delimeter + 1):
                if needle[j:delimeter + 1] in prefix_set:
                    prefix_table[delimeter] = delimeter - j + 1
                    break
                j += 1
            delimeter += 1
        return prefix_table


    '''

    '''
    def kmpSearch(self, haystack, needle):
        '''
        m: The position within S where the prospective match for W begins
        i: Index of the currently considered character in W.
        '''
        haystack_len = len(haystack)
        needle_len = len(needle)
        if (needle_len > haystack_len) or (not haystack_len) or (not needle_len):
            return -1
        prefix_table = self.get_prefix_table(needle)
        m = i = 0
        while((i < needle_len) and (m < haystack_len)):
            if haystack[m] == needle[i]:
                i += 1
                m += 1
            else:
                if i != 0:
                    i = prefix_table[i - 1]
                else:
                    m += 1
        if i == needle_len and haystack[m - 1] == needle[i - 1]:
            return m - needle_len
        else:
            return -1


class BoyerMoore(object):
    """docstring forBoyerMoore."""

    def __init__(self, haystack, needle):
        self.haystack = haystack
        self.needle = needle

    NO_OF_CHARS = 256

    def badCharHeuristic(self, string, size):
        '''
        The preprocessing function for
        Boyer Moore's bad character heuristic
        '''

        # Initialize all occurrence as -1
        badChar = [-1] * self.NO_OF_CHARS

        # Fill the actual value of last occurrence
        for i in range(size):
            badChar[ord(string[i])] = i

        # retun initialized list
        return badChar

    def search(self, txt, pat):
        '''
        A pattern searching function that uses Bad Character
        Heuristic of Boyer Moore Algorithm
        '''
        m = len(pat)
        n = len(txt)

        # create the bad character list by calling
        # the preprocessing function badCharHeuristic()
        # for given pattern
        badChar = self.badCharHeuristic(pat, m)

        # s is shift of the pattern with respect to text
        s = 0
        while(s <= n - m):
            j = m - 1

            # Keep reducing index j of pattern while
            # characters of pattern and text are matching
            # at this shift s
            while j >= 0 and pat[j] == txt[s + j]:
                j -= 1

            # If the pattern is present at current shift,
            # then index j will become -1 after the above loop
            if j < 0:
                return s
                s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
            else:
                s += max(1, j - badChar[ord(txt[s + j])])


class RabinKarp(object):
    """docstring for RabinKarp."""

    def __init__(self, haystack, needle):
        # superKMP_search, self).__init__()
        self.haystack = haystack
        self.needle = needle

    def hash(self, text):
        hash_value = 0
        for i in range(0, len(text)):
            hash_value += ord(text[i])**i
        return hash_value

    def rabinKarp(self):
        for i in range(len(self.haystack)-len(self.needle)+1):
            if self.hash(self.haystack[i:i+len(self.needle)]) == self.hash(self.needle):
                if self.haystack[i:i+len(self.needle)] == self.needle:
                    return i
        return -1


if __name__ == '__main__':
    needle = 'abcaby'
    haystack = 'nabxabcabcabylhghg'
    bruteForce = BruteForce(haystack, needle, start_indx = 0, found_indx = 0)
    kmp = KMP_search(haystack, needle)
    boyer = BoyerMoore(haystack, needle)
    rabin = RabinKarp(haystack, needle)
    print(rabin.rabinKarp())
    print(bruteForce.brute_force(haystack, needle))
    print(boyer.search(haystack, needle))
    print(kmp.kmpSearch(haystack, needle))
