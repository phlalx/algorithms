#TAGS stack, parenthesis


def match(c):
    if c == "(":
        return ")"
    elif c == "{":
        return "}"
    elif c == "[":
        return "]"
    else:
        assert False


def is_valid(s):
    stack = []
    for i in s:
        if i in ["(", "[", "{"]:
            stack.append(i)
        elif stack and match(stack.pop()) == i:
            pass
        else:
            return False
    return not stack


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return is_valid(s)
