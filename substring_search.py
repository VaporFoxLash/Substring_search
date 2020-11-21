
def get_prefix_table(needle):
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


def KMP_search(haystack, needle):
    '''
    m: The position within S where the prospective match for W begins
    i: Index of the currently considered character in W.
    '''
    haystack_len = len(haystack)
    needle_len = len(needle)
    if (needle_len > haystack_len) or (not haystack_len) or (not needle_len):
        return -1
    prefix_table = get_prefix_table(needle)
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


NO_OF_CHARS = 256


def badCharHeuristic(string, size):
    '''
    The preprocessing function for
    Boyer Moore's bad character heuristic
    '''

    # Initialize all occurrence as -1
    badChar = [-1] * NO_OF_CHARS

    # Fill the actual value of last occurrence
    for i in range(size):
        badChar[ord(string[i])] = i

    # retun initialized list
    return badChar


def search(txt, pat):
    '''
    A pattern searching function that uses Bad Character
    Heuristic of Boyer Moore Algorithm
    '''
    m = len(pat)
    n = len(txt)

    # create the bad character list by calling
    # the preprocessing function badCharHeuristic()
    # for given pattern
    badChar = badCharHeuristic(pat, m)

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


if __name__ == '__main__':
    needle = 'abcaby'
    haystack = 'nabxabcabcabyl'
    print(KMP_search(haystack, needle))
    search(haystack, needle)
