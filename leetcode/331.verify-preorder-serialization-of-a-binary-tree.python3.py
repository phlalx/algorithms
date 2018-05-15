# TAGS parser, tree, pythonic


class Error(BaseException):
    pass


def parse(iterator):

    # initialize invariant
    cur = next(iterator, None)

    def parse_tree():
        # cur is first non processed element
        nonlocal cur
        if cur is None:
            raise Error
        elif cur == "#":
            cur = next(iterator, None)
        else:
            assert cur.isnumeric()
            cur = next(iterator, None)
            parse_tree()
            parse_tree()

    parse_tree()

    return cur is None


class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        iterator = iter(preorder.split(","))
        try:
            return parse(iterator)
        except Error:
            return False
