class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf4 = [None] * 4
        i = 0
        n_read = 1
        while n > 0 and n_read:
            n_read = read4(buf4)
            n_read = min(n_read, n)
            buf[i : i + n_read] = buf4[:n_read]
            i += n_read
            n -= n_read
        return i
