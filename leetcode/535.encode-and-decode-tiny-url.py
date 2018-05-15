#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#
# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
#
# algorithms
# Medium (77.55%)
# Likes:    569
# Dislikes: 1250
# Total Accepted:    94.2K
# Total Submissions: 119.9K
# Testcase Example:  '"https://leetcode.com/problems/design-tinyurl"'
#
# Note: This is a companion problem to the System Design problem: Design
# TinyURL.
# 
# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such
# as http://tinyurl.com/4e9iAk.
# 
# Design the encode and decode methods for the TinyURL service. There is no
# restriction on how your encode/decode algorithm should work. You just need to
# ensure that a URL can be encoded to a tiny URL and the tiny URL can be
# decoded to the original URL.
# 
#

# @lc code=start

import string

PREFIX = "http://tinyurl.com/"
TINY_URL_CHARS = string.ascii_letters + string.digits

# encode counter to base len(TINY_URL_CHARS)
def _counter_tostring(c):
    res = []
    while c > 0:
        d = c % len(TINY_URL_CHARS)
        res.append(TINY_URL_CHARS[d])
        c = c // len(TINY_URL_CHARS)
    # note that res may be empty if c == 0
    # we could treat this particular case, or simply
    # start counting at 1
    return "".join(res)


class Codec:
    def __init__(self):
        self._counter = 1  # next value to use for encoding
        self._d = {}

    def _next_url(self):
        url = _counter_tostring(self._counter)
        self._counter += 1
        return url

    def encode(self, longUrl):
        tiny = self._next_url()
        self._d[tiny] = longUrl
        return PREFIX + tiny

    def decode(self, shortUrl):
        assert shortUrl.startswith(PREFIX)
        return self._d[shortUrl[len(PREFIX) :]]

class Solution:
    def __init__(self):
        self._counter = 1  # next value to use for encoding
        self._d = {}

    def _next_url(self):
        url = _counter_tostring(self._counter)
        self._counter += 1
        return url

    def encode(self, longUrl):
        tiny = self._next_url()
        self._d[tiny] = longUrl
        return PREFIX + tiny

    def decode(self, shortUrl):
        assert shortUrl.startswith(PREFIX)
        return self._d[shortUrl[len(PREFIX) :]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end

# TAGS bytes, pythonic

# Careful: this is not a base conversion from bytes to base58
#
# We keep a global counter of URL and encode each URL to a
# base-n encoded version of the counter
#
# We keep a map from tiny URL to their decoded form.
# The map keys don't keep the prefix `https://tinyurl.com`
#
# We could also avoid re-encoding by keeping a second map
#
#
# Reminder on byte objects
#
# Bytes object
#
# example of literal b'ab00\x23\013uv'
# to and from string, need to specify the encoding
# bytes('toto', encoding='ascii')
# str(0b'\012\023', encoding='ascii')
#   careful not to forget the encoding when using bytes, if not specified
#   str returns the byte literal such as printed by `print`.
#
# (bad but correct) Solution 1: just a change of encoding
#
# def _encode(s):
#     b = bytes(s, 'ascii')
#     return b.hex()  # note that hex(b) doesnt work on bytes

# def _decode(s):
#     b = bytes.fromhex(s)   # note that bytes(hex) doesn't work (obviously)
#     return str(b, 'ascii')

# class Solution:

#     def encode(self, longUrl):
#         return PREFIX + _encode(longUrl)

#     def decode(self, shortUrl):
#         assert shortUrl.startswith(PREFIX)
#         return _decode(shortUrl[len(PREFIX):])

def test():
    urls = ["https://leetcode.com/problems/design-tinyurl", "asdf", "asdfdsfl"]
    solution = Solution()
    for url in urls:
        enc = solution.encode(url)
        dec = solution.decode(enc)
        print(url, enc, dec)
    assert dec == url


if __name__ == "__main__":
    test()
