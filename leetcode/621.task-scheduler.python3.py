# TAGS greedy

# Tricky to get the right answer
#
# Suppose A has the maximal count, we will have tasks greedily organized
# as:
#
# A _ _ _ A _ _ _ A _ _ _ A _ _ _ A
#   idle
#
# duration = (m - 1) * (idle + 1) + 1
#
# If B has maximal count too,
#
# A B _ _ A B _ _ A _ _ _ A _ _ _ A B
#   idle
#
# duration = (m - 1) * (idle + 1) + mct
#
# Now two cases
#
# We can fit remaining tasks in the hole, and duration is known
# (we are sure that idle time will be respected).
#
# Otherwise, there's no hole, and answer is exactly n
#

import collections


class Solution:
    def leastInterval(self, tasks, idle):
        """
        :type tasks: List[str]
        :type idle: int
        :rtype: int
        """
        n = len(tasks)
        task_counts = collections.Counter(tasks).values()
        m = max(task_counts)
        # number of tasks with max count
        mct = sum(1 for t in task_counts if t == m)
        res = max(n, (m - 1) * (idle + 1) + mct)
        return res
