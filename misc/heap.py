# Heap datastructure
# Remember
#  - almost-complete binary tree, store as an array
#  - operations implemented using siftdown, siftup
#  - siftup is easy
#  - siftdown requires more care (easy if written the right way)
#  - heapify uses siftdown (O(n) complexity instead of O(n.log(n)))
#    for siftup
# TODO heapify

def parent(i):
    return (i - 1) // 2

def left(i):
    return 2*i + 1

def right(i):
    return 2 * i + 2

def siftup(l, i):
    while i > 0 and l[i] > l[parent(i)]:
        l[i], l[parent(i)] = l[parent(i)], l[i]
        i = parent(i)

def siftdown(nums, i):  # simpler to do it recursively
    n = len(nums)
    l = left(i)
    r = right(i)
    j = None
    v = nums[i]
    if l < n and nums[l] > v:
        j = l
    if r < n and nums[r] > v and nums[r] > nums[l]:
        j = r
    if j is not None:
        nums[j], nums[i] = nums[i], nums[j]
        siftdown(nums, j)

def insert(l, x):
    l.append(x)
    siftup(l, len(l) - 1)

def remove_max(l):
    assert len(l) >= 1
    res = l[0]
    l[0] = l[-1]
    l.pop()
    if l:
        siftdown(l, 0)
    return res

v = [5,1,2,4,3, 10, 7]
heap = []
for x in v:
    insert(heap, x)
print(heap)

res = [remove_max(heap) for _ in v]
print(res)
assert len(heap) == 0






