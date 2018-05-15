#TAGS serialization, string

def extract_int(s, i):
    res = 0
    while i < len(s) and s[i].isdigit():
        res += 10 * res + int(s[i])
        i += 1
    return res, i

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        n = str(len(strs))
        prefix = [str(n), '#']
        for s in strs:
            prefix.append(str(len(s)))
            prefix.append('#')
        return ''.join(prefix + strs)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        i = 0
        n, i = extract_int(s, i)
        i += 1 # skip '#'
        sizes = []
        for _ in range(n):
            size, i = extract_int(s, i)
            sizes.append(size)
            i += 1  # skip '#'
        res = []
        for size in sizes:
            res.append(s[i: i+size])
            i += size
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
