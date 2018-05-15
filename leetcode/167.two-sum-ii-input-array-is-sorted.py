#TAGS 2-sum, double pointer

class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)
        i = 0
        j = n - 1
        while i < j and (numbers[i] + numbers[j]) != target:
            cur = numbers[i] + numbers[j]
            if cur < target:
                i += 1
            else:
                j -= 1
        return [i+1, j+1]
