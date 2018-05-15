
# TODO delete, pred, succ
#
# We need a handle for deletion of a specific node, and
# access to parent pointer. Unless all keys are distinct
#
#
# we need to compute the parent for pred/succ
# see exercise "iterator for BST", compare solution where
# we iterate using an iterative DFS, and the one where we compute
# sequentially each successor

# Version 1
#
# Imperative style

def test():
    bst = None
    ar = [13, 5, 3, 2, 4, 7]
    for x in ar:
        bst = insert(bst, x)
    for x in ar:
        assert lookup(bst, x)

class Bst:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(bst, x):
    # TODO imperative

def lookup(bst, x):
    while bst:
        if bst.val == x:
            return True
        elif x < bst.val:
            bst = bst.left
        else:
            bst = bst.right
    return False

test()

# Object-oriented

class Bst:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # There's a little annoyance here
    # If we want to insert in left/right subtrees, we need to make
    # sure that the subtree isn't None (terminate the recursion
    # before the None case)
    # or we could define a Leaf class (interpreter pattern)
    # TODO

# functional version

class Bst:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(bst, x):
    # Do we really need this None case?
    # We can consider a BST is never empty
    # (or use a sentinel if needed)
    # In that case we don't even need to return a value
    if bst is None:
        return Bst(x)
    if x < bst.val:
        return Bst(bst.val, insert(bst.left, x), bst.right)
    else:
        return Bst(bst.val, bst.left, insert(bst.right, x))
    return bst

def lookup(bst, x):
    if bst is None:
        return False
    elif x < bst.val:
        return lookup(bst.left, x)
    else:
        return lookup(bst.right, x)

test()