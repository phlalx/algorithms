# Iterator

In python, raises StopIteration exception when not found.

Mostly two methods to fill. The object state is a cursor on an underlying
structure. Need to think of a class invariant that tells where is the cursor
between each call.

```
class StringIterator:
    def __init__(self, compressedString):
        pass

    def _someInternalMethod(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
```

## Solution 1: hasNext constant time

We want the cursor to be where it should be so that a
call to `hasNext` returns in constant time. It means that `next` has to
replace the cursor after computing the next element (which is found in
constant time).

Sometimes, the cursor needs to be updated when instanciating the class. Probably
we can factorize a private method for that.


