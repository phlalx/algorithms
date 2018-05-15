# TAGS data structure, cool

# It must be that:
#   . we store values in a hash table (O(1) insert, delete)
#   . we store values in an array (O(1) random)
#
# Problem, delete from array is O(n) if we need a lookup a value
#
# Solution, we store index in hash table for array lookup / an delete in O(1)
#

import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.l = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        i = self.d.get(val)
        if i is None:
            return False
        assert 0 <= i < len(self.l)
        last_val = self.l[-1]
        if val != last_val:
            self.d[last_val] = i
            self.l[i] = last_val
        del self.d[val]
        _ = self.l.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if not self.l:
            return -1
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
