from collections import Counter

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ctr = Counter()

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """

        self.ctr[number] += 1

        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for v in self.ctr:
            vv = value - v
            if v != vv and vv in self.ctr:
                return True
            if v == vv and self.ctr[vv] > 1:
                return True
        return False
 


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)