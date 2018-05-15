# segment tree

# TODO redo using array to store tree, and dynamic update

def build_seg(nums, i, j):
    if i == j:
        return Node( (nums[i], i) )
    else:
        t1 = build_seg(nums, i, (i+j) // 2)
        t2 = build_seg(nums, (i+j) // 2 + 1, j)
        return Node(max(t1.val, t2.val), t1, t2)

# compute max for nums[i:j+1]
def f(t, i, j, ti, tj):
    assert ti <= i <= j <= tj
    if (i, j) == (ti, tj):
        return t.val
    m = (ti + tj) // 2
    if j <= m:
        return f(t.left, i, j, ti, m)
    elif i >= m + 1:
        return f(t.right, i, j, m+1, tj)
    else:
        return max(f(t.left, i, m, ti, m), f(t.right, m+1, j, m+1, tj))



heights = [1,3,2,4,10]
n = len(heights)

##  TODO what is the size of this tree?
tree = [ None for _ in range(2 * n + 2) ]
# define these macros right away
left = lambda i: 2 * i + 1
right = lambda i: 2 * i + 2
root = 0

# TODO compare this tree with a tree produced by binary search
#      we cut in two adjacent parts, and not in three
def build_tree(i, j, node):
    assert 0 <= i <= j <= n - 1
    if i < j:
        m = (i + j) // 2
        build_tree(i, m, left(node))
        build_tree(m+1, j, right(node))
        # no need to return values
        m1 = tree[left(node)]
        m2 = tree[right(node)]
        tree[node] = min(m1, m2)
    else:
        # recursion stops at length 1 intervals
        assert i == j
        tree[node] = heights[i]

build_tree(0, n-1, root)

# We need to store the bounds of the tree, not only the query
def st_min(i, j, ti, tj, node):
    assert ti <= i <= j <= tj
    if (i, j) == (ti, tj):
        return tree[node]
    m = (ti + tj) // 2  # Not (i + j) // 2
    if j <= m:
        return st_min(i, j, ti, m, left(node))
    elif i >= m + 1:
        return st_min(i, j, m+1, tj, right(node))
    else:
        return min(st_min(i, m, ti, m, left(node)),
                    st_min(m+1, j, m+1, tj, right(node)))
    assert 0

def my_min(i, j):
    return st_min(i, j, 0, n-1, root)

print(my_min(4,n-1))
