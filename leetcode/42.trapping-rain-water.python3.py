class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = [(float("inf"), None)]
        n = len(height)
        pred = [None] * n
        for (i, v) in enumerate(height):
            last = (None, None)
            while stack[-1][0] <= v:
                last = stack.pop()
            if len(stack) >= 2:
                pred[i] = stack[-1][1]
            else:
                pred[i] = last[1]

            stack.append((v, i))

        res = 0
        i = n - 1
        while i > 0:
            p = pred[i]
            a = height[i]
            if p is None:
                i -= 1
                continue
            b = height[p]
            i0 = i
            i -= 1
            x = 0
            while i > p:
                x += height[i]
                i -= 1
            res += (i0 - p - 1) * min(a, b) - x
            i = p

        return res
