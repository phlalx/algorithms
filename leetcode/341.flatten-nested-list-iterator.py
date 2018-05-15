# TAGS iterator, data structure, stack
# see 173

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


def update_stack(s):
    while True:
        if not s:
            return
        n = s[-1]
        if isinstance(n, NestedInteger) and n.isInteger():
            return
        s.pop()
        if isinstance(n, NestedInteger):
            li = n.getList()
        else:
            li = n
        s.extend(reversed(li))


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [nestedList]
        update_stack(self.stack)

    def next(self):
        """
        :rtype: int
        """
        res = self.stack.pop().getInteger()
        update_stack(self.stack)
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

# Solution using python built-in types
#
# # Iterative DFS, in-order (easy because no node values, all orders
# # are equivalent)
# def f(l):
#     st = [l]
#     while st:
#         x = st.pop()
#         if type(x) is int:
#             print(x)
#         else:
#             st.extend(reversed(x))

# # cheating, using yield. f(l) is an iterator
# def f(l):
#     st = [l]
#     while st:
#         x = st.pop()
#         if type(x) is int:
#             yield x
#         else:
#             st.extend(reversed(x))

# # the real iterator
# class iterator:

#     def __init__(self, l):
#         self.st = [l]

#     def __next__(self):
#         if not self.st:
#             raise StopIteration
#         while self.st:
#             x = self.st.pop()
#             if type(x) is int:
#                 return x
#                 # no continuation after return, it would be more difficult
#                 # otherwise
#             else:
#                 self.st.extend(reversed(x))

#     def __iter__(self):
#         return self
