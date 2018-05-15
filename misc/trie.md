# Trie

A trie is a general tree, where each edge is indexed by a letter. It can be
implemented as a dictionary. Or if we want to store some aditional information
 (such as if a word belongs to the trie - useful for internal nodes), the
 simplest way is to inherit from dict.

Also better to use iterative functions. The python `dict.setdefault` is
convenient.

```
class Trie(dict):
    # little trick, extends dict and keep a word to avoid reconstructing
    # it later, and to know if a node corresponds to a word
    def __init__(self, word=None):
        # in which case we need a word instead of a bool?
        self.word = word


def insert(trie, w):
    for c in w:
        trie = trie.setdefault(c, Trie())
    trie.word = w

def search(trie, w):
    for c in w:
        trie = trie.get(c)
        if trie is None:
            return False
    return trie.word is not None
```

Even simpler

```
 trie['word'] = word   # don't bother with a class Trie to store this addditional
 ```

 See 140