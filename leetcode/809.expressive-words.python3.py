#TAGS double pointer, implementation
#
# Problem is hard to understand. Clearer statement:
# w is stretchy if
#  a group of letter can increase in size, but if so, should be at least
# three letters 

def char_num(w):
    pred = w[0]
    count = 0
    for c in w:
        if c != pred:
            yield pred, count
            count = 0
        count += 1
        pred = c
    yield pred, count

def stretchy(w, S):
    it1 = iter(char_num(w))
    it2 = iter(char_num(S))
    for (a, num_a), (b, num_b) in zip(it1, it2):
        if a != b:
            return False
        if num_a > num_b:
            return False
        if num_a != num_b and (num_b < 3):
            return False
    return next(it1, None) is None  and next(it2, None) is None


# Generators are probably overkill here
# without generators
def stretchy(w, S):
    i = 0
    j = 0
    n = len(w)
    p = len(S)
    while i < n:
        if j == p or w[i] != S[j]:
            return False
        ii = i
        while i < n and w[i] == w[ii]:
            i += 1
        jj = j
        while j < p and S[j] == S[jj]:
            j += 1
        a = i - ii
        b = j - jj
        if a > b or (a != b and (b < 3)):
            return False
    return j == p

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        return sum(stretchy(w, S) for w in words)


