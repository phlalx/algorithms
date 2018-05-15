# TAGS parser

# we need to discriminate between the possible cases for a byte
def extract(b):
    if not (b & 128):
        return 0
    if not (b & 64):
        return None
    if not (b & 32):
        return 1
    if not (b & 16):
        return 2
    if not (b & 8):
        return 3
    return None


class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if data == []:
            return True
        it = iter(data)
        cur = next(it)
        while cur is not None:
            # (usual) invariant, cur is the first non read byte
            n = extract(cur)
            if n is None:
                return False
            if n == 0:
                cur = next(it, None)
            else:  # 1 <= n <= 3:
                cur = next(it, None)
                while n >= 1 and cur:
                    if cur >> 6 != 2:
                        return False
                    cur = next(it, None)
                    n -= 1
                if n != 0:
                    return False
        return True
