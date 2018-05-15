# TAGS interval


def parse(log):
    id, isStart, t = log.split(":")
    id = int(id)
    isStart = isStart == "start"
    t = int(t)
    return id, isStart, t


class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        time = [0] * n
        stack = []
        cur_time = 0
        cur_fun = None

        for log in logs:
            id, isStart, t = parse(log)
            if not isStart:
                t = t + 1

            if cur_fun is not None:
                time[cur_fun] += t - cur_time

            if isStart:
                stack.append(id)
                cur_fun = id
            else:
                assert id == stack.pop()
                cur_fun = stack[-1] if len(stack) > 0 else None

            cur_time = t

        return time


def test():
    n = 2
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    solution = Solution()
    res = solution.exclusiveTime(n, logs)
    print(res)
    assert res == [3, 4]


test()
