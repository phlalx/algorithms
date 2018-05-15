# TREES

class Node:

    def __init__(self, v, left=None, right=None):
        self.left = left
        self.right = right
        self.v = v

    def children(self):
        return [self.left, self.right]

tree = Node(1, Node(2, Node(4, Node(5), Node(6))), Node(3, Node(7), Node(8)))

def walk_prefix(tree, res):
    if tree is None:
        return
    res.append(tree.v)
    walk_prefix(tree.left, res)
    walk_prefix(tree.right, res)

def walk_postfix(tree, res):
    if tree is None:
        return
    walk_postfix(tree.left, res)
    walk_postfix(tree.right, res)
    res.append(tree.v)

def walk_infix(tree, res):
    if tree is None:
        return
    walk_infix(tree.left, res)
    res.append(tree.v)
    walk_infix(tree.right, res)

def wrapper(walk, tree):
    res = []
    walk(tree, res)
    return res

def walk_iter_prefix(tree):
    res = []
    st = [ tree ]
    while st:
        node  = st.pop()
        if node is None:
            continue
        res.append(node.v)
        st.extend(reversed(node.children()))
    return res

# TODO check wiki implem, postfix traversal
def walk_iter_infix(tree):
    res = []
    st = []
    n = tree
    while n:
        st.append(n)
        n = n.left
    while st:
        n = st.pop()
        res.append(n.v)
        n = n.right
        while n:
            st.append(n)
            n = n.left
    return res

res = wrapper(walk_infix, tree)
print(res)
print(walk_iter_infix(tree))



