# TAGS datatype, lexer


class StringIterator:
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.compressedString = compressedString
        self.i = 0
        self.cur_char = None
        self.n = len(compressedString)
        self.cur_count = 0

    def _getint(self):
        j = self.i
        cc = 0
        while j < self.n and self.compressedString[j].isdigit():
            cc = 10 * cc + int(self.compressedString[j])
            j += 1
        return j, cc

    def next(self):
        """
        :rtype: str
        """
        if self.cur_count > 0:
            self.cur_count -= 1
            return self.cur_char
        elif self.i < self.n:
            self.cur_char = self.compressedString[self.i]
            self.i += 1
            self.i, self.cur_count = self._getint()
            assert self.cur_count
            self.cur_count -= 1
            return self.cur_char
        else:
            return " "

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur_count > 0 or self.i < self.n


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
