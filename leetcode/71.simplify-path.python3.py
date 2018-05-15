# TAGS string


def simplify(elts):
    res = []
    for elt in elts:
        if elt == "..":
            if res:
                res.pop()
        elif elt != "." and elt != "":
            res.append(elt)
    return res


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        elts = path.split("/")
        simpl = simplify(elts)
        res = "/".join(simpl)
        return "/" + res
